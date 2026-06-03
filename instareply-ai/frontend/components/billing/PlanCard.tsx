type PlanCardProps = {
  name: string;
  price: string;
};

export function PlanCard({ name, price }: PlanCardProps) {
  return (
    <article className="rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
      <h2 className="text-lg font-bold">{name}</h2>
      <p className="mt-2 text-2xl font-bold text-indigo-600">{price}</p>
      <button className="mt-4 w-full rounded-lg bg-indigo-600 px-4 py-2 text-sm font-semibold text-white" type="button">
        Upgrade
      </button>
    </article>
  );
}
