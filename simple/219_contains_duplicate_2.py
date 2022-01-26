"""
分为前后两个数组？前面的数组为k个，后面数组也为k个，做个字典？

"""
from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left_d = defaultdict(int)
        right_d = defaultdict(int)
        # 最初是设置一个初始状态，右边的字典是前某些数
        for i in range(min(len(nums),k)):
            # left_d[nums[i]] = 1
            right_d[nums[i]] = 1
        for i in range(len(nums)):
            if i <= k:
                right_d[nums[i]] -= 1 if right_d[nums[i]] >= 1 else 0
                if i + k < len(nums):
                    right_d[nums[i+k]] += 1
                if right_d[nums[i]] > 0 or left_d[nums[i]] > 0:
                    return True
                left_d[nums[i]] += 1
            elif k < i < len(nums) - k:
                right_d[nums[i]] -= 1 if right_d[nums[i]] >= 1 else 0
                left_d[nums[i-k-1]] -= 1 if left_d[nums[i-k-1]] >= 1 else 0
                # if i + k < len(nums):
                right_d[nums[i+k]] += 1
                if right_d[nums[i]] > 0 or left_d[nums[i]] > 0:
                    return True
                left_d[nums[i]] += 1
            elif len(nums)-k < i < len(nums):
                right_d[nums[i]] -= 1 if right_d[nums[i]] >= 1 else 0
                left_d[nums[i - k-1]] -= 1 if left_d[nums[i - k-1]] >= 1 else 0
                # if i + k < len(nums):
                # right_d[nums[i+k]] += 1
                if right_d[nums[i]] > 0 or left_d[nums[i]] > 0:
                    return True
                left_d[nums[i]] += 1
        return False

demo = Solution()
print(demo.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))