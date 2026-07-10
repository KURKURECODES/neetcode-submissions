import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxh=[]
        for i in range(len(stones)):
            heapq.heappush(maxh,-stones[i])
        while(len(maxh)>1):
            val1=-heapq.heappop(maxh)
            val2=-heapq.heappop(maxh)
            val1=val1-val2
            heapq.heappush(maxh,-val1)
        return -maxh[0]
        