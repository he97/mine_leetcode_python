import sys
from typing import List


class Solution:
    # 使用level记录每个数字的层次在用二分查找 方便定位
    def findNumberOfLIS(self, nums: List[int]) -> int:
        count = 1
        dp = []
        if len(nums) == 0:
            return 0
        dp.append([1, 1])
        for i in range(1,len(nums)):
            count = 0
            max_level = -1
            for j in range(len(dp)):
                if dp[j][0] > max_level and nums[j] < nums[i]:
                    max_level = dp[j][0]
            for j in range(len(dp)):
                if dp[j][0] == max_level and nums[j] < nums[i]:
                    count += dp[j][1]
            dp.append([max(max_level+1, 1),max(count, 1)])
        result = 0
        max_level = -1
        for j in range(len(dp)):
            if dp[j][0] > max_level:
                max_level = dp[j][0]
                result = dp[j][1]
            elif dp[j][0] == max_level:
                result += dp[j][1]
        return result

demo = Solution()
print(demo.findNumberOfLIS([2,2,2,2,2]))


