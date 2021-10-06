from collections import defaultdict
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = defaultdict(int)
        for i in range(len(paths)):
            if d[paths[i][0]] == 1:
                d[paths[i][0]] = 0
            else:
                d[paths[i][0]] = 1
            if d[paths[i][1]] == 1:
                d[paths[i][1]] = 0
            else:
                d[paths[i][1]] = 1
        c = []
        for i in d.keys():
            if d[i] != 0:
                c.append(i)
        for i in range(len(paths)):
            if paths[i][0] == c[0]:
                return c[1]
            if paths[i][0] == c[1]:
                return c[0]


demo = Solution()
print(demo.destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))