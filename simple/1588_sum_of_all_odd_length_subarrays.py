# 给你一个正整数数组arr，请你计算所有可能的奇数长度子数组的和。
#
# 子数组 定义为原数组中的一个连续子序列。
#
# 请你返回 arr中 所有奇数长度子数组的和 。
#
#
# 输入：arr = [1,4,2,5,3]
# 输出：58
# 解释：所有奇数长度子数组和它们的和为：
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# 我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                count += sum(arr[i:j+1])
        return count

demo = Solution()
print(demo.sumOddLengthSubarrays(arr = [1,4,2,5,3]))
