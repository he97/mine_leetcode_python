from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        low = 0
        high = n-1
        mid = (low + high) // 2
        if n == 0:
            return [-1, -1]
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if nums[mid] == target:
            a = mid
            c = 0
            d = 0
            while a >= 0 and nums[a] == target:
                c = a
                a -= 1
            a = mid
            while a < n and nums[a] == target:
                d = a
                a += 1
            return [c, d]
        else:
            return [-1, -1]

demo = Solution()
print(demo.searchRange([2,2],3))
print(demo.searchRange([1,3],1))
print(demo.searchRange([2,2],2))
print(demo.searchRange([1],1))
print(demo.searchRange(nums = [5,7,7,8,8,10], target = 8))