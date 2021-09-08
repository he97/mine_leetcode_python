# 给你一个与 nums大小相同且初始值全为 0 的数组 arr ，请你调用以上函数得到整数数组 nums。
#
# 请你返回将 arr变成 nums的最少函数调用次数。
#
# 答案保证在 32 位有符号整数以内。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-numbers-of-function-calls-to-make-target-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import math
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while True:
            tag = False
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    nums[i] -= 1
                    count += 1
                if nums[i] > 0:
                    tag = True
            if tag:
                count += 1
                for i in range(len(nums)):
                    if nums[i] > 0:
                        nums[i] = math.floor(nums[i]/2)
            else:
                break
        return count


demo = Solution()
print(demo.minOperations(nums = [1,5]))
print(demo.minOperations(nums = [2,2]))
print(demo.minOperations(nums = [4,2,5]))
print(demo.minOperations(nums = [3,2,2,4]))
print(demo.minOperations(nums = [2,4,8,16]))


