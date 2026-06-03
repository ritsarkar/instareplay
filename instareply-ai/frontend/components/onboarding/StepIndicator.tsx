type StepIndicatorProps = {
  currentStep: number;
  totalSteps: number;
};

export function StepIndicator({ currentStep, totalSteps }: StepIndicatorProps) {
  const percent = (currentStep / totalSteps) * 100;

  return (
    <div>
      <p className="text-sm font-semibold text-indigo-600">Step {currentStep} of {totalSteps}</p>
      <div className="mt-3 h-2 overflow-hidden rounded-full bg-slate-100">
        <div className="h-full rounded-full bg-indigo-600" style={{ width: `${percent}%` }} />
      </div>
    </div>
  );
}
