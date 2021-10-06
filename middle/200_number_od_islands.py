from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visit[i][j]:
                    count += 1
                    d = []
                    for direc in direction:
                        a = i + direc[0]
                        b = j + direc[1]
                        if 0 <= a < m and 0 <= b < n and grid[a][b] == '1' and not visit[a][b]:
                            d.append([a,b])
                            visit[a][b] = True
                    while len(d) > 0:
                        temp = []
                        for edge in d:
                            for direc in direction:
                                a = edge[0] + direc[0]
                                b = edge[1] + direc[1]
                                if 0 <= a < m and 0 <= b < n and grid[a][b] == '1' and not visit[a][b]:
                                    temp.append([a, b])
                                    visit[a][b] = True
                        d = temp
        return count


demo = Solution()
print(demo.numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))
