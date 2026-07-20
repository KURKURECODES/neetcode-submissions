from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # Build adjacency list
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        # Distance array
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        # Min Heap -> (current_distance, node)
        heap = [(0, k)]

        while heap:

            curr_dist, node = heapq.heappop(heap)

            # Ignore outdated entries
            if curr_dist > dist[node]:
                continue

            # Relax all neighbors
            for nei, weight in adj[node]:

                new_dist = curr_dist + weight

                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))

        answer = max(dist[1:])

        if answer == float('inf'):
            return -1

        return answer