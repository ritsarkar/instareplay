export type ConversationState = "new" | "active" | "waiting_for_human" | "human_active" | "resolved" | "snoozed";

export type Plan = "free" | "starter" | "pro" | "agency";

export interface User {
  id: string;
  name: string;
  email: string;
  plan: Plan;
  onboarding_step: number;
}
