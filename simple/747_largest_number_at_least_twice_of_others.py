import sys
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first = second = -1
        for i in range(len(nums)):
            if first == second == -1:
                first = i
            elif first != -1 and second == -1:
                if nums[i] > nums[first]:
                    second = first
                    first = i
                else:
                    second = i
            else:
                if nums[i] > nums[first]:
                    second = first
                    first = i
                elif nums[i] > nums[second]:
                    second = i
        if second == -1:
            return first
        elif nums[first] >= 2 * nums[second]:
            return first
        else:
            return -1
