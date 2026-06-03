type MessageBubbleProps = {
  align: "left" | "right";
  text: string;
};

export function MessageBubble({ align, text }: MessageBubbleProps) {
  const alignment = align === "right" ? "ml-auto bg-indigo-600 text-white" : "mr-auto bg-white text-slate-700";

  return <div className={`max-w-sm rounded-xl px-4 py-3 text-sm shadow-sm ${alignment}`}>{text}</div>;
}
