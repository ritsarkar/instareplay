type UsageBarProps = {
  used: number;
  limit: number;
};

export function UsageBar({ used, limit }: UsageBarProps) {
  const percent = limit > 0 ? Math.min((used / limit) * 100, 100) : 0;

  return (
    <div className="h-2 overflow-hidden rounded-full bg-slate-100">
      <div className="h-full rounded-full bg-indigo-600" style={{ width: `${percent}%` }} />
    </div>
  );
}
