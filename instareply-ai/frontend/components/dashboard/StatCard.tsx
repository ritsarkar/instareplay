type StatCardProps = {
  label: string;
  value: string;
  trend: string;
};

export function StatCard({ label, value, trend }: StatCardProps) {
  return (
    <article className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
      <p className="text-sm font-medium text-slate-500">{label}</p>
      <div className="mt-3 flex items-end justify-between gap-4">
        <span className="text-3xl font-bold text-slate-900">{value}</span>
        <span className="text-sm font-semibold text-emerald-600">{trend}</span>
      </div>
    </article>
  );
}
