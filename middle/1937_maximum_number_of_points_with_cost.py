# 给你一个m x n的整数矩阵points（下标从 0开始）
# 一开始你的得分为 0，你想最大化从矩阵中得到的分数。
#
# 你的得分方式为：每一行中选取一个格子，
# 选中坐标为(r, c)的格子会给你的总得分 增加points[r][c]。
#
# 然而，相邻行之间被选中的格子如果隔得太远，你会失去一些得分。
# 对于相邻行r 和r + 1（其中0 <= r < m - 1），
# 选中坐标为(r, c1) 和(r + 1, c2)的格子，你的总得分减少abs(c1 - c2)。
#
# 请你返回你能得到的 最大得分。
#
# abs(x)定义为：
#
# 如果x >= 0，那么值为x。
# 如果x <0，那么值为 -x。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-number-of-points-with-cost
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        for i in range(1, m):
            s = points[i].copy()
            best = float('-inf')
            for j in range(n):
                best = max(best, points[i-1][j] + j)
                points[i][j] = max(points[i][j], best + s[j] - j)
            best = float('-inf')
            for j in range(n-1,-1,-1):
                best = max(best, points[i - 1][j] - j)
                points[i][j] = max(points[i][j], best + s[j] + j)
                # points[i][j] = max(points[i - 1][k] + points[i][j] - abs(k - j) for k in range(n))

        return max(points[m-1])


demo = Solution()
print(demo.maxPoints([[1, 2, 3], [1, 5, 1], [3, 1, 1]]))
print(demo.maxPoints([[1,5],[2,3],[4,2]]))
print(demo.maxPoints([[1,5],[2,3],[4,2]]))
