# 给你一个整数 n 。按下述规则生成一个长度为 n + 1 的数组 nums ：
#
# nums[0] = 0
# nums[1] = 1
# 当 2 <= 2 * i <= n 时，nums[2 * i] = nums[i]
# 当 2 <= 2 * i + 1 <= n 时，nums[2 * i + 1] = nums[i] + nums[i + 1]
# 返回生成数组 nums 中的 最大 值。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/get-maximum-in-generated-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = [-1 for _ in range(n + 1)]

        for i in range(n+1):
            if i == 0 and memo[i] == -1:
                memo[i] = 0
            elif i == 1 and memo[i] == -1:
                memo[i] = 1
            if 2 <= 2 * i <= n and memo[2 * i] == -1:
                memo[2 * i] = memo[i]
            if 2 <= 2 * i + 1 <= n and memo[2 * i + 1] == -1:
                memo[2 * i + 1] = memo[i] + memo[i + 1]

        a = max(memo)
        return a


demo = Solution()
print(demo.getMaximumGenerated(7))
print(demo.getMaximumGenerated(15))
print(demo.getMaximumGenerated(2))
print(demo.getMaximumGenerated(3))
print(demo.getMaximumGenerated(0))
print(demo.getMaximumGenerated(1))
