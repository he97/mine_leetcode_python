from typing import List

from sortedcontainers import SortedList


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        result = SortedList()
        if k ==0:
            return []
        for i in range(len(arr)):
            if len(result) < k:
                result.add(arr[i])
            elif arr[i] < result[-1]:
                result.pop()
                result.add(arr[i])
        return list(result)
demo = Solution()
print(demo.smallestK([1,2,3]
,0))
print(demo.smallestK(arr = [1,3,5,7,2,4,6,8], k = 4))