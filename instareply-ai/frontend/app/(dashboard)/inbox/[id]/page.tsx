import { MessageThread } from "@/components/inbox/MessageThread";

export default function ConversationDetailPage() {
  return (
    <section className="space-y-6">
      <h1 className="text-2xl font-bold">Conversation</h1>
      <MessageThread />
    </section>
  );
}
