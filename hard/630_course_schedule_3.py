import heapq
from typing import List

from sortedcontainers import SortedList


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        cnt, heap = 0, []
        for c in courses:
            if cnt + c[0] <= c[1]:
                heapq.heappush(heap, -c[0])
                cnt += c[0]
            elif heap:
                max_val = -heapq.heappop(heap)
                heapq.heappush(heap, -min(c[0], max_val))
                cnt = cnt - max_val + min(c[0], max_val)
        return len(heap)


demo = Solution()
print(demo.scheduleCourse([[9, 14], [7, 12], [1, 11], [4, 7]]))
print(demo.scheduleCourse([[3, 2], [4, 3]]))
print(demo.scheduleCourse([[5, 5], [4, 6], [2, 6]]))
print(demo.scheduleCourse([[1, 2], [2, 3]]))
print(demo.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
