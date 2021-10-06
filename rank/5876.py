import heapq
from typing import List

from sortedcontainers import SortedList


class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = SortedList(nums[2:])
        # heap = []
        # for i in range(2,len(nums)):
        #     heapq.heappush(heap, nums[i])
        count = 0
        big = nums[0]
        low = s[0]
        for i in range(1, len(nums)-1):
            if i > 1:
                s.remove(nums[i])
            if low == nums[i]:
                low = s[0]
            if big < nums[i] < low:
                count += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                count += 1
            if nums[i] > big:
                big = nums[i]



            # if low == nums[i]:

        return count

demo = Solution()
print(demo.sumOfBeauties([1,2,3,4,5,6]))
print(demo.sumOfBeauties([1,2,3]))
print(demo.sumOfBeauties([2,4,6,4]))
print(demo.sumOfBeauties([3,2,1]))
