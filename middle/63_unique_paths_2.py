# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
#
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-paths-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        direction = [[0,1],[1,0]]
        # 找一个矩阵
        z = min(m,n)
        y = max(m,n)
        d = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[m-1][n-1]!=1:
            d[m-1][n-1] = 1
        # if m-1 and n-2 > 0:
        #     d[m-1][n-2] = 1
        # if m-2 and n-1 > 0:
        #     d[m-2][n-1] = 0
        # 先把矩阵的dp写好
        for i in range(1,z):
            for j in range(i):
                a = m-1-j
                b = n-1-i
                if obstacleGrid[a][b]!=1:
                    for direc in direction:
                        if a + direc[0] < m and b + direc[1]<n:
                            d[a][b] += d[a + direc[0]][b + direc[1]]
            for j in range(i):
                a = m - 1 - i
                b = n - 1 - j
                if obstacleGrid[a][b] != 1:
                    for direc in direction:
                        if a + direc[0] < m and b + direc[1] < n:
                            d[a][b] += d[a + direc[0]][b + direc[1]]
            a = m - 1 - i
            b = n - 1 - i
            if obstacleGrid[a][b] != 1:
                for direc in direction:
                    if a + direc[0] < m and b + direc[1] < n:
                        d[a][b] += d[a + direc[0]][b + direc[1]]
        # 左边还有多余的
        if m == z and n > z:
            for i in range(z,n):
                b = n-1-i
                for j in range(m-1,-1,-1):
                    a = j
                    if obstacleGrid[a][b] != 1:
                        for direc in direction:
                            if a + direc[0] < m and b + direc[1] < n:
                                d[a][b] += d[a + direc[0]][b + direc[1]]
        # 上边还有多余的
        elif n == z and m > z:
            for i in range(z,m):
                a = m-1-i
                for j in range(n-1,-1,-1):
                    b = j
                    if obstacleGrid[a][b] != 1:
                        for direc in direction:
                            if a + direc[0] < m and b + direc[1] < n:
                                d[a][b] += d[a + direc[0]][b + direc[1]]
        return d[0][0]
demo = Solution()
print(demo.uniquePathsWithObstacles([[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]))
print(demo.uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))
print(demo.uniquePathsWithObstacles(obstacleGrid = [[0,0],[0,1]]))


