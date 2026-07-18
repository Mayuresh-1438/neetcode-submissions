from _heapq import heapify,heappop,heappush
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for p in points:
            x,y = p
            dist = x**2 + y**2
            heappush(heap,(-dist,p))
            if len(heap) > k:
                heappop(heap)
        for _,p in heap:
            res.append(p)
        return res