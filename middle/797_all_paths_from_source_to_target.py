# 给你一个有n个节点的 有向无环图（DAG），请你找出所有从节点 0到节点 n-1的路径并输出（不要求按特定顺序）
# 
# 二维数组的第 i 个数组中的单元都表示有向图中 i 号节点所能到达的下一些节点，空就是没有下一个结点了。
# 
# 译者注：有向图是有方向的，即规定了 a→b 你就不能从 b→a 。
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/all-paths-from-source-to-target
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        def get_paths(index)-> List[List[int]]:
            temp = []
            for i in range(len(graph[index])):
                if graph[index][i] == n-1:
                    temp.append([n-1,index])
                else:
                    b = get_paths(graph[index][i])
                    for j in b:
                        j.append(index)
                        temp.append(j)

            return temp
        a = get_paths(0)
        for i in a:
            i.reverse()
        return a


demo = Solution()
print(demo.allPathsSourceTarget(graph = [[1,2],[3],[3],[]]))