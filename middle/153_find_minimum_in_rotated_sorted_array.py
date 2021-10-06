from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            tag = True
            if mid - 1 >= 0:
                if nums[mid-1] < nums[mid]:
                    tag = False
            if mid + 1 < len(nums) and tag:
                if nums[mid+1] < nums[mid]:
                    tag = False
            if tag:
                return nums[mid]
            if nums[mid] < nums[low]:
                high = mid - 1
            elif nums[mid] > nums[high]:
                low = mid + 1
            elif nums[low] <= nums[mid] <= nums[high]:
                return nums[low]

demo = Solution()
print(demo.findMin(nums = [3,4,5,1,2]))
print(demo.findMin(nums = [4,5,6,7,0,1,2]))



