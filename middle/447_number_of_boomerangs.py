import math
from collections import defaultdict
from typing import List

from scipy.special import comb, perm


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        m = len(points)
        d = [[0 for _ in range(m)] for _ in range(m)]
        count = 0
        for i in range(0, m):
            for j in range(i + 1, m):
                dis = math.sqrt(abs(points[i][0] - points[j][0]) ** 2 + abs(points[i][1] - points[j][1]) ** 2)
                d[i][j] = dis
                d[j][i] = dis
        for i in range(m):
            diction = defaultdict()
            for j in range(m):
                if d[i][j] not in diction.keys():
                    diction[d[i][j]] = 1
                else:
                    diction[d[i][j]] += 1
            for k in diction.keys():
                if diction[k] >= 2:
                    count += int(comb(diction[k], 2) * 2)
        return count


demo = Solution()
print(demo.numberOfBoomerangs(points=[[0, 0], [1, 0], [2, 0]]))
print(demo.numberOfBoomerangs(points=[[1, 1], [2, 2], [3, 3]]))
print(demo.numberOfBoomerangs(points=[[1, 1]]))
