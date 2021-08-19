from collections import defaultdict
from typing import List


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[defaultdict(int) for i in range(n)] for j in range(m)]
        all_count = 0
        next_level = [[startRow, startColumn]]
        for i in range(m):
            dp[i][0][1] += 1
            dp[i][n-1][1] += 1
        for j in range(n):
            dp[0][j][1] += 1
            dp[m-1][j][1] += 1
        min_index = 0
        if startRow > min_index > startColumn:
            min_index = startColumn + 1
        else:
            min_index = startRow + 1
        index = 1

        def add_point(i: int, k: int) -> List[List[int]]:
            temp = []
            temp.append([i - 1, k])
            temp.append([i + 1, k])
            temp.append([i, k - 1])
            temp.append([i, k + 1])
            return temp

        def get_path(l: List[List[int]], move: int) -> int:
            count = 0
            if move > 0:
                for i in l:
                    if 0 <= i[0] < m and 0 <= i[1] < n:
                        if dp[i[0]][i[1]][move] != 0:
                            count += dp[i[0]][i[1]][move]
                        elif move >= min(i[0] + 1, i[1] + 1, m - i[0], n - i[1]):
                            points = add_point(i[0], i[1])
                            dp[i[0]][i[1]][move] = get_path(points, move - 1)
                            count += dp[i[0]][i[1]][move]
                        else:
                            continue
            return count

        while index <= maxMove:
            foot = index
            all_count += get_path([[startRow, startColumn]], foot)
            index += 1
        return all_count % (pow(10,9) + 7)


demo = Solution()
print(demo.findPaths(2,3,8,1,0))
