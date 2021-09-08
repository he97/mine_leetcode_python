# 在给定的二维二进制数组 A 中，存在两座岛。
# （岛是由四面相连的 1 形成的一个最大组。）
#
# 现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。
#
# 返回必须翻转的 0 的最小数目。（可以保证答案至少是 1 。）

from collections import defaultdict
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        d = [[0 for i in range(n)]for i in range(n)]
        island = 1
        direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        next_level = []
        temp = []
        edges_1 = []
        edges_2 = []
        bridge = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if d[i][j] == 0 and grid[i][j] == 1:
                    d[i][j] = island
                    for direc in direction:
                        if 0 <= i + direc[0] < n and 0 <= j + direc[1] < n and \
                                d[i + direc[0]][j + direc[1]] == 0 and grid[i + direc[0]][j + direc[1]] == 1:
                            d[i + direc[0]][j + direc[1]] = island
                            next_level.append([i + direc[0], j + direc[1]])
                    while len(next_level) > 0:
                        for index in range(len(next_level)):
                            i_index = next_level[index][0]
                            j_index = next_level[index][1]
                            for direc in direction:
                                if 0 <= i_index + direc[0] < n and 0 <= j_index + direc[1] < n and \
                                        d[i_index + direc[0]][j_index + direc[1]] == 0 and \
                                        grid[i_index + direc[0]][j_index + direc[1]] == 1:
                                    d[i_index + direc[0]][j_index + direc[1]] = island
                                    temp.append([i_index + direc[0], j_index + direc[1]])
                        next_level = temp
                        temp = []
                    island += 1
        for i in range(n):
            for j in range(n):
                for direc in direction:
                    if 0 <= i + direc[0] < n and 0 <= j + direc[1] < n and\
                            d[i + direc[0]][j + direc[1]] == 0:
                        if d[i][j] == 1:
                            edges_1.append([i, j])
                            break
                        elif d[i][j] == 2:
                            edges_2.append([i, j])
                            break
        while True:
            temp = []
            for i in range(len(edges_1)):
                i_index = edges_1[i][0]
                j_index = edges_1[i][1]
                for direc in direction:
                    if 0 <= i_index + direc[0] < n and 0 <= j_index + direc[1] < n and \
                            d[i_index + direc[0]][j_index + direc[1]] == 0:
                        d[i_index + direc[0]][j_index + direc[1]] = 1
                        temp.append([i_index + direc[0], j_index + direc[1]])
                    elif 0 <= i_index + direc[0] < n and 0 <= j_index + direc[1] < n and \
                            d[i_index + direc[0]][j_index + direc[1]] == 2:
                        return bridge
            edges_1 = temp
            bridge += 1
            temp = []
            for i in range(len(edges_2)):

                i_index = edges_2[i][0]
                j_index = edges_2[i][1]
                for direc in direction:
                    if 0 <= i_index + direc[0] < n and 0 <= j_index + direc[1] < n and \
                            d[i_index + direc[0]][j_index + direc[1]] == 0:
                        d[i_index + direc[0]][j_index + direc[1]] = 2
                        temp.append([i_index + direc[0], j_index + direc[1]])
                    elif 0 <= i_index + direc[0] < n and 0 <= j_index + direc[1] < n and \
                            d[i_index + direc[0]][j_index + direc[1]] == 1:
                        return bridge
            edges_2 = temp
            bridge += 1


demo = Solution()
print(demo.shortestBridge([[1,1,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
print(demo.shortestBridge([[0, 1], [1, 0]]))
print(demo.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
print(demo.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
print(demo.shortestBridge(grid=[[0, 1, 1, 1, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]]))
