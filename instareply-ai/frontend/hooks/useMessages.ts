import { useQuery } from "@tanstack/react-query";

export function useMessages(conversationId?: string) {
  return useQuery({
    enabled: Boolean(conversationId),
    queryKey: ["messages", conversationId],
    queryFn: async () => [],
  });
}
