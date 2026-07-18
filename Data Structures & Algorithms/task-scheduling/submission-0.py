from _heapq import heapify, heappop,heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        maxHeap = []
        q = deque()
        time = 0
        for i in tasks:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic.values():
            maxHeap.append(-i)
        heapify(maxHeap)
        while maxHeap or q:
            time +=1
            if maxHeap:
                cnt = 1 + heappop(maxHeap)
                if cnt:
                    q.append([cnt,n + time])
            if q and q[0][1] == time:
                heappush(maxHeap,q.popleft()[0])
        return time