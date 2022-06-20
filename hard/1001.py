'''
先设置一个row
下面的方案时间复杂度过高
由官方的方法可以知道根据一个坐标就可以判定主对角线和反对角线
'''
from collections import defaultdict
from typing import List


class Solution:
    def gridIllumination(self,
                         n: int,
                         lamps: List[List[int]],
                         queries: List[List[int]]) -> List[int]:
        d_row = defaultdict(bool)
        d_row_count = defaultdict(int)
        d_column = defaultdict(bool)
        d_column_count = defaultdict(int)
        d = defaultdict(bool)
        res = []
        direc = [[-1, -1], [-1, 0], [-1, 1],
                 [0, -1], [0, 1], [1, -1], [1, 0], [1, 1],[0,0]]
        lamps_set = []
        for i in lamps:
            if not d[str(i[0])+str(i[1])]:
                d_row_count[i[0]] += 1
                d_column_count[i[1]] += 1
                d_row[i[0]] = True
                d_column[i[1]] = True
                d[str(i[0])+str(i[1])] = True
                lamps_set.append(i)
        for i in queries:
            if d_row[i[0]] is True:
                res.append(1)
            elif d_column[i[1]] is True:
                res.append(1)
            else:
                tag = False
                for x in lamps_set:
                    if d[str(x[0])+str(x[1])] and abs(i[0] - x[0]) == abs(i[1] - x[1]):
                        tag = True
                        break
                res.append(1) if tag else res.append(0)
            for x in direc:
                if 0 <= i[0] + x[0] < n and 0 <= i[1] + x[1] < n:
                    z = [i[0] + x[0], i[1] + x[1]]
                    if d[str(z[0])+str(z[1])]:
                        d[str(z[0])+str(z[1])] = False
                        d_row_count[z[0]] -= 1
                        if d_row_count[z[0]] == 0:
                            d_row[z[0]] = False
                        d_column_count[z[1]] -= 1
                        if d_column_count[z[1]] == 0:
                            d_column[z[1]] = False
        return res

demo = Solution()
print(demo.gridIllumination(100
,[[7,55],[53,61],[2,82],[67,85],[81,75],[38,91],[68,0],[60,43],[40,19],[12,75],[26,2],[24,89],[42,81],[60,58],[77,72],[33,24],[19,93],[7,16],[58,54],[78,57],[97,49],[65,16],[42,75],[90,50],[89,34],[76,97],[58,23],[62,47],[94,28],[88,65],[3,87],[81,10],[12,81],[44,81],[54,92],[90,54],[17,54],[27,82],[48,15],[8,46],[4,99],[15,13],[90,77],[2,87],[18,33],[52,90],[4,95],[57,61],[31,22],[32,8],[49,26],[24,65],[88,55],[88,38],[64,76],[94,76],[59,12],[41,46],[80,28],[38,36],[65,67],[75,37],[56,97],[83,57],[2,4],[44,43],[71,90],[62,40],[79,94],[81,11],[96,34],[38,11],[22,3],[54,96],[78,33],[54,54],[79,98],[1,28],[0,32],[37,11]]
,[[24,84],[95,68],[80,35],[31,53],[69,45],[85,29],[87,25],[42,47],[7,59],[99,3],[31,70],[64,62],[44,91],[55,25],[15,52],[95,33],[21,29],[61,34],[93,34],[79,27],[30,86],[52,0],[18,10],[5,1],[40,21],[11,48],[55,94],[22,42],[81,0],[39,43],[5,25],[43,29],[45,47],[83,93],[77,70],[22,63],[30,73],[18,48],[39,88],[91,47]]))
print(demo.gridIllumination(6
,[[2,5],[4,2],[0,3],[0,5],[1,4],[4,2],[3,3],[1,0]]
,[[4,3],[3,1],[5,3],[0,5],[4,4],[3,3]]))
print(demo.gridIllumination(n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]))
