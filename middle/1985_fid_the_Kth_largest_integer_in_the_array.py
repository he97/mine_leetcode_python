import random
from collections import defaultdict
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        d = defaultdict()
        for i in nums:
            if int(i) not in d.keys():
                d[int(i)] = 1
            else:
                d[int(i)] += 1
        for j in sorted(d.keys(),reverse=True):
            if k > d[j]:
                k -= d[j]
            else:
                return str(j)


demo = Solution()
print(demo.kthLargestNumber(["3","6","7","10"]
,4)
)
print(demo.kthLargestNumber(nums=['1','1'],k=1))
print(demo.kthLargestNumber(nums=['0','0'],k=2))
print(demo.kthLargestNumber(nums = ["2","21","12","1"], k = 3))
