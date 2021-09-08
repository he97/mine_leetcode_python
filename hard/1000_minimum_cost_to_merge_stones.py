# 有 N 堆石头排成一排，第 i 堆中有stones[i]块石头。
# 
# 每次移动（move）需要将连续的K堆石头合并为一堆，而这个移动的成本为这K堆石头的总数。
# 
# 找出把所有石头合并成一堆的最低成本。如果不可能，返回 -1 。
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-cost-to-merge-stones
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import math
import sys
from typing import List


# class Solution:
#     def mergeStones(self, stones: List[int], k: int) -> int:
#         n = len(stones)
#
#         p = n
#         while p / k >= 1:
#             p = math.floor(p / k) + p % k
#         if p != 1:
#             return -1
#         c = self.get_min_join(stones, 0, k)
#         return c
#
#     def get_min_join(self, stones, cost, k) -> int:
#         m = len(stones)
#         if m >= k:
#             min_index = 0
#             min_count = sys.maxsize
#             temp = 0
#             for i in range(0, m - k + 1):
#                 if i == 0:
#                     j = 0
#                     while j < k:
#                         temp += stones[j]
#                         j += 1
#                     # d[i] = temp
#                     # temp -= stones[i]
#                     a = stones.copy()
#                     a[i] = temp
#                     del a[i + 1:i + k]
#                     b = self.get_min_join(a, cost + temp, k)
#                     if min_count > b:
#                         min_count = b
#                     temp -= stones[i]
#                 else:
#                     if i + k <= m:
#                         temp += stones[i + k - 1]
#                         a = stones.copy()
#                         a[i] = temp
#                         del a[i + 1:i + k]
#                         b = self.get_min_join(a, cost + temp, k)
#                         if min_count > b:
#                             min_count = b
#                         temp -= stones[i]
#                 i += 1
#             return min_count
#         else:
#             return cost
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n-1) % (k-1) != 0:
            return -1
        presum = [0 for _ in range(n +1)]
        for i in range(n):
            presum[i+1] = presum[i] + stones[i]

        dp = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][i] = 0

        for delta in range(1,  n + 1):
            for L in range(1, n + 1 - delta):
                R = L + delta
                for mid in range(L, R, k - 1):
                    dp[L][R] = min(dp[L][R], dp[L][mid] + dp[mid+1][R])
                if delta % (k - 1) == 0:
                    dp[L][R] += (presum[R] - presum[L-1]);

        return dp[1][n]

demo = Solution()
print(demo.mergeStones([69,39,79,78,16,6,36,97,79,27,14,31,4]
,2))
print(demo.mergeStones(stones=[6, 4, 4, 6], k=2))
print(demo.mergeStones(stones=[3, 2, 4, 1], k=2))
print(demo.mergeStones(stones=[3, 2, 4, 1], k=3))
print(demo.mergeStones(stones=[3, 5, 1, 2, 6], k=3))
