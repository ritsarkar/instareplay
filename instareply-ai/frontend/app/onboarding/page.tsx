import { StepIndicator } from "@/components/onboarding/StepIndicator";

export default function OnboardingPage() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-slate-50 p-6">
      <section className="w-full max-w-xl rounded-xl border border-slate-200 bg-white p-6 shadow-sm">
        <StepIndicator currentStep={1} totalSteps={6} />
        <h1 className="mt-6 text-2xl font-bold">Business Profile</h1>
        <p className="mt-2 text-slate-500">The complete six-step onboarding flow will be wired in Phase 11.</p>
      </section>
    </main>
  );
}
