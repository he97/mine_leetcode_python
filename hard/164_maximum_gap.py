# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
#
# 如果数组元素个数小于 2，则返回 0。
import heapq
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap, i)
        prev = -1
        gap = 0
        while len(heap) > 0:
            a = heapq.heappop(heap)
            if prev == -1:
                prev = a
            else:
                if a - prev > gap:
                    gap = a - prev
                prev = a
        return gap


demo = Solution()
print(demo.maximumGap([3,6,9,1]))