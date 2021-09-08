from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
                if high < 0:
                    return -1
            elif nums[mid] < target:
                low = mid + 1
                if low >= len(nums):
                    return -1
        return -1

demo = Solution()
print(demo.search([-1,0,3,5,9,12]
,13))
