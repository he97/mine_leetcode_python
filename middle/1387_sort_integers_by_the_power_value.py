# 我们将整数 x的 权重 定义为按照下述规则将 x变成 1所需要的步数：
#
# 如果x是偶数，那么x = x / 2
# 如果x是奇数，那么x = 3 * x + 1
# 比方说，x=3 的权重为 7 。因为 3 需要 7 步变成 1 （3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1）。
#
# 给你三个整数lo，hi 和k。你的任务是将区间[lo, hi]之间的整数按照它们的权重升序排序，如果大于等于 2 个整数有相同的权重，那么按照数字自身的数值升序排序。
#
# 请你返回区间[lo, hi]之间的整数按权重排序后的第k个数。
#
# 注意，题目保证对于任意整数x（lo <= x <= hi），它变成1 所需要的步数是一个 32 位有符号整数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sort-integers-by-the-power-value
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import math
from collections import defaultdict


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = defaultdict(int)

        def sear(num: int) -> int:
            if num == 1:
                return 1
            else:
                if num % 2 == 0:
                    if dp[math.floor(num / 2)] == 0:
                        depth = sear(math.floor(num / 2))
                    else:
                        depth = dp[math.floor(num / 2)] + 1
                else:
                    if dp[3 * num + 1] == 0:
                        depth = sear(3 * num + 1)
                    else:
                        depth = dp[3 * num + 1] + 1
                if dp[num] == 0:
                    dp[num] = depth
                return depth + 1

        for i in range(lo, hi + 1):
            sear(i)

        # dp[1] = 0
        # step = 1
        # c = [1]
        # while len(c) > 0:
        #     temp = []
        #     for j in range(len(c)):
        #         if c[j]*2 < n and dp[c[j]*2] == -1:
        #             dp[c[j]*2] = step
        #             temp.append(c[j]*2)
        #         if (c[j]-1) % 3 == 0 and dp[int((c[j]-1) / 3)] == -1 and int((c[j]-1) / 3) > 0 and int((c[j]-1) / 3) % 2 == 1:
        #             dp[int((c[j]-1) / 3)] = step
        #             temp.append(int((c[j]-1) / 3))
        #     step += 1
        #     c = temp
        # for x in range(10000):
        #     if dp[x] == -1:
        #         print('dp[{0}]:{1}'.format(x, dp[x]))
        # vv = [1,2,4,8,16,5,10,20,40,13,26,52,17,34,11,22,7,14,28,9]
        # for x in vv:
        #     print('dp[{0}]:{1}'.format(x,dp[x]))
        s = []
        for i in range(lo, hi + 1):
            s.append([dp[i], i])
        dp = s
        while len(dp) > 0:
            pivot = dp[0]
            low = []
            high = []
            for i in range(1, len(dp)):
                if dp[i][0] < pivot[0]:
                    low.append(dp[i])
                else:
                    high.append(dp[i])
            if k == len(low) + 1:
                return pivot[1]
            elif len(low) >= k:
                dp = low
            else:
                dp = high
                k -= (len(low) + 1)


# a = 703
# print(a)
# xx = 0
# z = 0
# while a != 1:
#     if a % 2 == 1:
#         a = 3 * a + 1
#         if a > z:
#             z = a
#     else:
#         a = int(a / 2)
#     xx += 1
#     print(a)
# print('xx:', xx)
# print('z:', z)

demo = Solution()
print(demo.getKth(lo=7, hi=11, k=4))
print(demo.getKth(lo=12, hi=1000, k=2))
