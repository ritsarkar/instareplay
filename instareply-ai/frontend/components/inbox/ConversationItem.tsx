type ConversationItemProps = {
  name: string;
  preview: string;
};

export function ConversationItem({ name, preview }: ConversationItemProps) {
  return (
    <button className="flex w-full gap-3 border-b border-slate-100 p-4 text-left hover:bg-slate-50" type="button">
      <span className="grid h-10 w-10 shrink-0 place-items-center rounded-full bg-indigo-100 font-semibold text-indigo-700">
        {name.slice(0, 1)}
      </span>
      <span className="min-w-0">
        <span className="block truncate text-sm font-semibold text-slate-900">{name}</span>
        <span className="block truncate text-sm text-slate-500">{preview}</span>
      </span>
    </button>
  );
}
