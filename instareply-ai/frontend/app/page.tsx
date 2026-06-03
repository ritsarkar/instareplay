import Link from "next/link";

export default function HomePage() {
  return (
    <main className="min-h-screen bg-slate-50 px-6 py-10 text-slate-900">
      <section className="mx-auto flex max-w-5xl flex-col gap-6">
        <p className="text-sm font-semibold uppercase tracking-wide text-indigo-600">
          InstaReply AI
        </p>
        <h1 className="max-w-3xl text-4xl font-bold leading-tight md:text-6xl">
          AI-powered Instagram DM automation for Indian businesses
        </h1>
        <p className="max-w-2xl text-lg text-slate-600">
          Phase 1 scaffold is ready. The dashboard, backend services, and integrations will be filled in phase by phase.
        </p>
        <div className="flex flex-wrap gap-3">
          <Link className="rounded-lg bg-indigo-600 px-4 py-2 font-semibold text-white" href="/dashboard">
            Open dashboard
          </Link>
          <Link className="rounded-lg border border-slate-300 px-4 py-2 font-semibold text-slate-700" href="/login">
            Login
          </Link>
        </div>
      </section>
    </main>
  );
}
