from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        if nums[low] == target:
            return low
        if nums[high] == target:
            return high
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] == target:
                return low
            if nums[high] == target:
                return high
            # 在两个递增序列中的较大的内部
            if nums[mid] >= nums[low] and nums[mid] >= nums[high]:
                if nums[mid] < target:
                    low = mid + 1
                elif nums[high] >= target and nums[mid] > target:
                    low = mid + 1
                else:
                    high = mid - 1
            elif nums[mid] <= nums[low] and nums[mid] <= nums[high]:
                if nums[mid] > target:
                    high = mid - 1
                elif nums[low] <= target and nums[mid] < target:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[low] <= nums[mid] <= nums[high]:
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


demo = Solution()
print(demo.search([3,4,5,1,2],4))
print(demo.search([4,5,6,7,8,1,2,3],8))
print(demo.search([1,3],3))
print(demo.search(nums = [4,5,6,7,0,1,2], target = 0))
print(demo.search(nums = [4,5,6,7,0,1,2], target = 3))
print(demo.search(nums = [1], target = 0))