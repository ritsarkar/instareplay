export default function CustomersPage() {
  return (
    <section className="space-y-6">
      <div className="flex items-center justify-between gap-4">
        <h1 className="text-2xl font-bold">Customers</h1>
        <button className="rounded-lg border border-slate-200 bg-white px-4 py-2 text-sm font-semibold">Export</button>
      </div>
      <div className="rounded-xl border border-slate-200 bg-white p-6 text-slate-500">Customer records will appear here.</div>
    </section>
  );
}
