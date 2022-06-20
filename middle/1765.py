"""
从洼地开始，设置洼地为0
高度差至多为1，也就是说当确定一个点时，其上下左右的高度为其+-0
哈曼顿距离
每个点的距离为到每个洼点的哈曼顿距离的最小值
那么如果水域的点太多 会造成时间消耗过多 如何解决呢
距离为1 [[0,-1],[0,1],[1,0],[-1,0]]
距离为4 [[0,-4],[0,4],[1]] 01 13 22 31 40

时间复杂度太高了 使用多源广度优先搜索 详情看题解去吧
"""
from collections import defaultdict
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        d = defaultdict(bool)
        direc = [[0,1],[0,-1],[1,0],[-1,0]]
        m = len(isWater)
        n = len(isWater[0])
        res = [[-1 for a_ in range(n)]for _ in range(m)]
        for i in range(m):
            for k in range(n):
                if isWater[i][k]==1:
                    a = [[i,k]]
                    depth = 0
                    while len(a)>0:
                        temp = []
                        for j in a:
                            if res[j[0]][j[1]] == -1 or res[j[0]][j[1]]> depth:
                                res[j[0]][j[1]] = depth
                                for x in direc:
                                    c = j[0]+x[0]
                                    d = j[1] + x[1]
                                    if 0<=c<m and 0<=d <n and (res[c][d]==-1 or res[c][d]>= depth):
                                        temp.append([c,d])
                        depth += 1
                        a = temp
        return res

demo = Solution()
print(demo.highestPeak([[0,1],[0,0]]))