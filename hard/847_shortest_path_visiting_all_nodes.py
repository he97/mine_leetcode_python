# 存在一个由 n 个节点组成的无向连通图，图中的节点按从 0 到 n - 1 编号。
#
# 给你一个数组 graph 表示这个图。其中，graph[i] 是一个列表，由所有与节点 i 直接相连的节点组成。
#
# 返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shortest-path-visiting-all-nodes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    # 找一条关键路径吗？没有权值

    def shortestPathLength(self, graph: List[List[int]]) -> int:
