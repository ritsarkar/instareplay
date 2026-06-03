import { useQuery } from "@tanstack/react-query";

export function useAnalytics() {
  return useQuery({
    queryKey: ["analytics"],
    queryFn: async () => ({}),
  });
}
