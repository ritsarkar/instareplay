type StateBadgeProps = {
  state: string;
};

export function StateBadge({ state }: StateBadgeProps) {
  return <span className="rounded-full bg-indigo-50 px-2 py-1 text-xs font-semibold text-indigo-700">{state}</span>;
}
