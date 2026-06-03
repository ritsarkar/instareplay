import { ConversationList } from "@/components/inbox/ConversationList";
import { MessageThread } from "@/components/inbox/MessageThread";

export default function InboxPage() {
  return (
    <section className="space-y-6">
      <h1 className="text-2xl font-bold">Inbox</h1>
      <div className="grid min-h-[640px] overflow-hidden rounded-xl border border-slate-200 bg-white md:grid-cols-[340px_1fr]">
        <ConversationList />
        <MessageThread />
      </div>
    </section>
  );
}
