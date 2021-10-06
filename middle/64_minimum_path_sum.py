# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
import sys
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        direction = [[-1, 0], [0, -1]]
        for i in range(min(m, n)):
            j = i
            k = i
            while j < n:
                for direc in direction:
                    a = i + direc[0]
                    b = j + direc[1]
                    if 0 <= a < m and 0 <= b < n:
                        if dp[a][b] + grid[i][j] < dp[i][j]:
                            dp[i][j] = dp[a][b] + grid[i][j]
                j += 1
            while k < m:
                for direc in direction:
                    a = k + direc[0]
                    b = i + direc[1]
                    if 0 <= a < m and 0 <= b < n:
                        if dp[a][b] + grid[k][i] < dp[k][i]:
                            dp[k][i] = dp[a][b] + grid[k][i]
                k += 1
        return int(dp[m - 1][n - 1])


demo = Solution()
print(demo.minPathSum(grid = [[1,2,3],[4,5,6]]))
print(demo.minPathSum(grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
