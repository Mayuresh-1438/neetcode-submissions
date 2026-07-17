from _heapq import heappush, heappop, heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heap.append(-i)
        heapify(heap)
        while len(heap) > 1:
            p = heappop(heap)
            q = heappop(heap)
            if q > p:
                heappush(heap,p-q)
        heap.append(0)        
        return abs(heap[0])