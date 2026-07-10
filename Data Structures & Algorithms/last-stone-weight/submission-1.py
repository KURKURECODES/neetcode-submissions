import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Build the max-heap (inverted min-heap) in O(N) time
        maxh = [-s for s in stones]
        heapq.heapify(maxh)
        
        # Keep smashing until 1 (or 0) stones are left
        while len(maxh) > 1:
            val1 = -heapq.heappop(maxh) # Heaviest stone
            val2 = -heapq.heappop(maxh) # Second heaviest
            
            # The remaining weight (if they are equal, this is 0)
            val1 = val1 - val2
            
            # Push the remaining stone back in as a negative
            heapq.heappush(maxh, -val1)
            
        # The last remaining element is our answer
        return -maxh[0]