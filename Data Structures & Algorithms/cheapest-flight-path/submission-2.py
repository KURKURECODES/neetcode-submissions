from typing import List
from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # Build adjacency list
        adj = defaultdict(list)

        for u, v, price in flights:
            adj[u].append((v, price))

        # dist[node][edges]
        # Minimum cost to reach 'node' using exactly 'edges' flights
        dist = [[float("inf")] * (k + 2) for _ in range(n)]

        # (cost, node, edges_used)
        heap = []

        heapq.heappush(heap, (0, src, 0))
        dist[src][0] = 0

        while heap:

            cost, node, edges = heapq.heappop(heap)

            # Destination reached
            if node == dst:
                return cost

            # Cannot take more flights
            if edges == k + 1:
                continue

            for nei, price in adj[node]:

                newCost = cost + price

                if newCost < dist[nei][edges + 1]:

                    dist[nei][edges + 1] = newCost

                    heapq.heappush(
                        heap,
                        (newCost, nei, edges + 1)
                    )

        return -1