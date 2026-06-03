import { MessageBubble } from "@/components/inbox/MessageBubble";

export function MessageThread() {
  return (
    <section className="flex min-h-[640px] flex-col bg-slate-50">
      <div className="border-b border-slate-200 bg-white p-4">
        <h2 className="font-semibold">Select a conversation</h2>
      </div>
      <div className="flex-1 space-y-3 p-4">
        <MessageBubble align="left" text="Messages will appear here once Instagram webhooks are connected." />
      </div>
    </section>
  );
}
