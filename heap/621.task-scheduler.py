from collections import Counter
from heapq import heappop, heappush, heapify
from typing import List
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-val for val in counts.values()]
        heapify(maxHeap) 
        queue = deque()
        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                count = heappop(maxHeap)
                if count + 1 < 0:   
                    queue.append([count+1, time+n])
            if queue and queue[0][1] == time:
                count, pos = queue.popleft()
                heappush(maxHeap, count)
        return time