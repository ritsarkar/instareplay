import { LucideIcon, TrendingUp, TrendingDown, Minus } from "lucide-react";

interface StatCardProps {
  title: string;
  value: string | number;
  icon: LucideIcon;
  trend?: {
    value: number;
    label: string;
  };
  trendDirection?: "up" | "down" | "neutral";
}

export function StatCard({ title, value, icon: Icon, trend, trendDirection = "neutral" }: StatCardProps) {
  return (
    <div className="group relative overflow-hidden rounded-2xl bg-white p-6 shadow-sm ring-1 ring-slate-200 transition-all duration-300 hover:shadow-md hover:-translate-y-1">
      <div className="absolute -right-6 -top-6 h-24 w-24 rounded-full bg-indigo-50/50 transition-transform duration-500 group-hover:scale-150"></div>
      
      <div className="relative flex items-start justify-between">
        <div>
          <p className="text-sm font-medium text-slate-500">{title}</p>
          <p className="mt-2 text-3xl font-bold tracking-tight text-slate-900">{value}</p>
        </div>
        <div className="rounded-xl bg-indigo-50 p-3 text-indigo-600 transition-colors group-hover:bg-indigo-100 group-hover:text-indigo-700">
          <Icon className="h-6 w-6" />
        </div>
      </div>
      
      {trend && (
        <div className="mt-4 flex items-center gap-2 text-sm">
          <div
            className={`flex items-center gap-1 rounded-full px-2 py-0.5 text-xs font-semibold ${
              trendDirection === "up"
                ? "bg-emerald-100 text-emerald-700"
                : trendDirection === "down"
                ? "bg-rose-100 text-rose-700"
                : "bg-slate-100 text-slate-700"
            }`}
          >
            {trendDirection === "up" && <TrendingUp className="h-3 w-3" />}
            {trendDirection === "down" && <TrendingDown className="h-3 w-3" />}
            {trendDirection === "neutral" && <Minus className="h-3 w-3" />}
            <span>{trendDirection === "up" ? "+" : trendDirection === "down" ? "-" : ""}{Math.abs(trend.value)}%</span>
          </div>
          <span className="text-slate-500">{trend.label}</span>
        </div>
      )}
    </div>
  );
}
