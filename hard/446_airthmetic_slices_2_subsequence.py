# 给你一个整数数组 nums ，返回 nums 中所有 等差子序列 的数目。
#
# 如果一个序列中 至少有三个元素 ，并且任意两个相邻元素之差相同，
# 则称该序列为等差序列。
#
# 例如，[1, 3, 5, 7, 9]、[7, 7, 7, 7] 和 [3, -1, -5, -9] 都是等差序列。
# 再例如，[1, 1, 2, 5, 7] 不是等差序列。
# 数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。
#
# 例如，[2,5,10] 是 [1,2,1,2,4,1,5,10] 的一个子序列。
# 题目数据保证答案是一个 32-bit 整数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 1  <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
from collections import defaultdict
from typing import List


# not in
# 先从前两个数查，
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        dp = [defaultdict(int) for _ in nums]
        for i in range(1, len(nums)):
            for j in range(0, i):
                interval = nums[i] - nums[j]
                a = dp[j][interval]
                count += a
                dp[i][interval] += a + 1
        return count
        # 用哈希数组是因为公差未知且数量可能比较大
        # defaultdict(int) 不存在时会默认提供整数零
        # f = [defaultdict(int) for _ in nums]
        # for i, x in enumerate(nums):
        #     for j in range(i):
        #         # d:公差
        #         d = x - nums[j]
        #         cnt = f[j][d]
        #         ans += cnt
        #         f[i][d] += cnt + 1
        # return ans
    #     # max_gap = max(nums) - min(nums)
    #     all_count = 0
    #
    #     # interval = [[1 for i in range(max_interval)]for i in range(max_interval)]
    #
    #     if len(nums) < 3:
    #         return 0
    #     for i in range(len(nums) - 2):
    #         for j in range(i + 1, len(nums) - 1):
    #             all_count += self.get_count(j, nums[j] - nums[i], nums=nums)
    #     return all_count
    #
    # def get_count(self, index: int, interval: int, nums: List[int]) -> int:
    #     recur_count = 0
    #     next_number = nums[index] + interval
    #     if next_number not in nums[index + 1:len(nums)]:
    #         return 0
    #     else:
    #         for inner_index in range(index + 1, len(nums)):
    #             if nums[inner_index] == next_number:
    #                 # print('进入递归，相等的下标是：{0}{1}'.format(index, inner_index))
    #                 recur_count += 1 + self.get_count(inner_index, interval,nums)
    #                 # print('inner_index:{0},count+1:{1}'.format(inner_index, count + 1))
    #     return recur_count


demo = Solution()
print(demo.numberOfArithmeticSlices([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
print(demo.numberOfArithmeticSlices([7, 7, 7, 7, 7]))
print(demo.numberOfArithmeticSlices([2, 4, 6, 8, 10]))
