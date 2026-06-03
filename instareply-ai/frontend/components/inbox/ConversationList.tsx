import { ConversationItem } from "@/components/inbox/ConversationItem";

export function ConversationList() {
  return (
    <aside className="border-r border-slate-200 bg-white">
      <div className="border-b border-slate-200 p-4">
        <h2 className="font-semibold">Conversations</h2>
      </div>
      <ConversationItem name="No conversations yet" preview="Incoming Instagram DMs will appear here." />
    </aside>
  );
}
