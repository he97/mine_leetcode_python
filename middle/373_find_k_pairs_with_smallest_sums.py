"""
如果暴力枚举的话，估计会超过时间限制
合最小
"""
from typing import List
from sortedcontainers import SortedList


class Solution:
    def kSmallestPairs(self,
                       nums1: List[int],
                       nums2: List[int],
                       k: int) -> List[List[int]]:
        c = SortedList(key=lambda x: x[0] + x[1])
        d = [0 for _ in range(len(nums1))]
        for i in range(len(d)):
            c.add([nums1[i], nums2[d[i]], i])
        result = []
        while len(result) < k:
            a = c.pop(0)
            result.append(a[0:2])
            if d[a[2]] + 1 < len(nums2):
                d[a[2]] += 1
                c.add([nums1[a[2]], nums2[d[a[2]]], a[2]])
        return result


demo = Solution()
print(demo.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3))
