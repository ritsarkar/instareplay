import { StatCard } from "@/components/ui/StatCard";
import { 
  MessageSquare, 
  Users, 
  Zap, 
  Clock 
} from "lucide-react";

export default function DashboardPage() {
  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-bold tracking-tight text-slate-900">Dashboard Overview</h1>
        <p className="text-slate-500 mt-1">Here's what's happening with your Instagram account today.</p>
      </div>

      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        <StatCard
          title="Total Messages"
          value="1,248"
          icon={MessageSquare}
          trend={{ value: 12, label: "vs last week" }}
          trendDirection="up"
        />
        <StatCard
          title="Active Conversations"
          value="42"
          icon={Users}
          trend={{ value: 4, label: "vs last week" }}
          trendDirection="down"
        />
        <StatCard
          title="AI Resolution Rate"
          value="89%"
          icon={Zap}
          trend={{ value: 2.5, label: "vs last week" }}
          trendDirection="up"
        />
        <StatCard
          title="Avg. Response Time"
          value="2.4s"
          icon={Clock}
          trend={{ value: 0.1, label: "vs last week" }}
          trendDirection="up"
        />
      </div>

      <div className="grid gap-6 lg:grid-cols-2">
        {/* Placeholder for Recent Activity */}
        <div className="rounded-2xl bg-white p-6 shadow-sm ring-1 ring-slate-200">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-lg font-semibold text-slate-900">Recent Activity</h2>
            <button className="text-sm font-medium text-indigo-600 hover:text-indigo-700">View all</button>
          </div>
          <div className="flex flex-col items-center justify-center py-12 text-center border-2 border-dashed border-slate-100 rounded-xl">
            <div className="h-12 w-12 rounded-full bg-slate-50 flex items-center justify-center mb-4">
              <MessageSquare className="h-6 w-6 text-slate-400" />
            </div>
            <p className="text-sm font-medium text-slate-900">No activity yet</p>
            <p className="text-sm text-slate-500 mt-1">Connect your Instagram account to see messages here.</p>
          </div>
        </div>

        {/* Placeholder for Quick Actions */}
        <div className="rounded-2xl bg-white p-6 shadow-sm ring-1 ring-slate-200">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-lg font-semibold text-slate-900">Quick Actions</h2>
          </div>
          <div className="space-y-4">
            <div className="group flex items-center justify-between rounded-xl border border-slate-200 p-4 transition-all hover:border-indigo-600 hover:shadow-sm cursor-pointer">
              <div className="flex items-center gap-4">
                <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-50 text-indigo-600 group-hover:bg-indigo-600 group-hover:text-white transition-colors">
                  <Zap className="h-5 w-5" />
                </div>
                <div>
                  <p className="font-medium text-slate-900">Connect Instagram</p>
                  <p className="text-sm text-slate-500">Link your professional account</p>
                </div>
              </div>
              <button className="rounded-full bg-slate-50 px-3 py-1 text-xs font-semibold text-slate-600 group-hover:bg-indigo-50 group-hover:text-indigo-600 transition-colors">Setup</button>
            </div>

            <div className="group flex items-center justify-between rounded-xl border border-slate-200 p-4 transition-all hover:border-indigo-600 hover:shadow-sm cursor-pointer">
              <div className="flex items-center gap-4">
                <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-50 text-indigo-600 group-hover:bg-indigo-600 group-hover:text-white transition-colors">
                  <Users className="h-5 w-5" />
                </div>
                <div>
                  <p className="font-medium text-slate-900">Upload Knowledge Base</p>
                  <p className="text-sm text-slate-500">Train AI with your FAQs</p>
                </div>
              </div>
              <button className="rounded-full bg-slate-50 px-3 py-1 text-xs font-semibold text-slate-600 group-hover:bg-indigo-50 group-hover:text-indigo-600 transition-colors">Add Data</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
