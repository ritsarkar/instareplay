"use client";

import { useEffect, useState } from "react";
import api from "@/lib/api";
import { Users, MessageSquare, Database, Activity } from "lucide-react";

interface AnalyticsData {
  total_customers: number;
  total_messages_processed: number;
  total_knowledge_documents: number;
  active_conversations: number;
  resolved_conversations: number;
}

export default function AnalyticsPage() {
  const [data, setData] = useState<AnalyticsData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAnalytics = async () => {
      try {
        const response = await api.get("/api/analytics");
        if (response.data.success) {
          setData(response.data.data);
        }
      } catch (error) {
        console.error("Failed to fetch analytics:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchAnalytics();
  }, []);

  if (loading) {
    return (
      <div className="flex h-[50vh] items-center justify-center">
        <div className="h-8 w-8 animate-spin rounded-full border-4 border-indigo-500 border-t-transparent"></div>
      </div>
    );
  }

  const stats = [
    {
      name: "Total Customers Engaged",
      value: data?.total_customers || 0,
      icon: Users,
      color: "text-blue-500",
      bgColor: "bg-blue-500/10",
    },
    {
      name: "Messages Processed by AI",
      value: data?.total_messages_processed || 0,
      icon: MessageSquare,
      color: "text-indigo-500",
      bgColor: "bg-indigo-500/10",
    },
    {
      name: "Active Conversations",
      value: data?.active_conversations || 0,
      icon: Activity,
      color: "text-emerald-500",
      bgColor: "bg-emerald-500/10",
    },
    {
      name: "Knowledge Documents",
      value: data?.total_knowledge_documents || 0,
      icon: Database,
      color: "text-purple-500",
      bgColor: "bg-purple-500/10",
    },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold tracking-tight text-white">Analytics Overview</h1>
        <p className="text-gray-400">Track your AI agent's performance and customer engagement.</p>
      </div>

      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
        {stats.map((stat) => {
          const Icon = stat.icon;
          return (
            <div
              key={stat.name}
              className="relative overflow-hidden rounded-xl border border-white/10 bg-white/5 p-6 backdrop-blur-lg transition-all hover:bg-white/10"
            >
              <div className="flex items-center gap-4">
                <div className={`rounded-lg p-3 ${stat.bgColor}`}>
                  <Icon className={`h-6 w-6 ${stat.color}`} />
                </div>
                <div>
                  <p className="text-sm font-medium text-gray-400">{stat.name}</p>
                  <p className="text-2xl font-bold text-white">{stat.value.toLocaleString()}</p>
                </div>
              </div>
              <div className="absolute -bottom-6 -right-6 opacity-10">
                <Icon className="h-24 w-24" />
              </div>
            </div>
          );
        })}
      </div>

      {/* Additional charts or detailed metrics can be added below here */}
      <div className="mt-8 rounded-xl border border-white/10 bg-white/5 p-6 backdrop-blur-lg">
        <h2 className="text-lg font-medium text-white mb-4">Conversation Metrics</h2>
        <div className="flex items-center justify-between border-b border-white/10 pb-4">
          <span className="text-gray-400">Total Conversations Resolved</span>
          <span className="font-semibold text-emerald-400">
            {data?.resolved_conversations || 0}
          </span>
        </div>
        <div className="flex items-center justify-between pt-4">
          <span className="text-gray-400">AI Resolution Rate</span>
          <span className="font-semibold text-indigo-400">
            {data?.total_customers ? "100%" : "0%"} {/* Placeholder logic */}
          </span>
        </div>
      </div>
    </div>
  );
}
