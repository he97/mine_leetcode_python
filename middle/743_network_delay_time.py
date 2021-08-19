# 有 n 个网络节点，标记为1到 n。
# 
# 给你一个列表times，表示信号经过 有向 边的传递时间。
# times[i] = (ui, vi, wi)，
# 其中ui是源节点，vi是目标节点， wi是一个信号从源节点传递到目标节点的时间。
# 
# 现在，从某个节点K发出一个信号。
# 需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回-1 。
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/network-delay-time
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import sys
from typing import List

# 已完成
# 迪杰斯特拉算法
class Solution:
    # n: count of nodes
    # k: start node
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        max_index = n
        # # 查找节点总数
        # for i in times:
        #     if i[0] > max_index or i[1] > max_index:
        #         if i[0] > i[1]:
        #             max_index = i[0]
        #         else:
        #             max_index = i[1]
        edges = [[]] * max_index
        # 为每个节点分配空间
        for i in range(0, max_index):
            edges[i] = []
        #     将边重新分配
        for i in times:
            edges[i[0] - 1].append(i)
        # 实现迪杰斯特拉算法
        # 设置一个辅助队列保存距离并初始化
        distance = [sys.maxsize] * max_index
        is_selected = [False] * max_index
        for i in range(0, len(distance)):
            i = sys.maxsize
        #       方便后面判别？
        distance[k - 1] = -1
        # 设置一个变量保存每次探测中最小的点,一个变量保存最短距离
        short_distance_node = k - 1
        short_distance = 0
        while True:
            for index in range(0, len(edges[short_distance_node])):
                if edges[short_distance_node][index][2] + short_distance < \
                        distance[edges[short_distance_node][index][1] - 1]:
                    distance[edges[short_distance_node][index][1] - 1] = \
                        int(edges[short_distance_node][index][2]) + short_distance
            short_distance_temp = short_distance
            max_dis = sys.maxsize
            find_new_short = False
            mini_index = 0
            for index in range(0, len(distance)):
                if short_distance_temp <= distance[index] <= max_dis:
                    if not is_selected[index]:
                        mini_index = index
                        if short_distance_node != index:
                            find_new_short = True
                        short_distance_node = index
                        short_distance = distance[index]
                        max_dis = distance[index]
            if not find_new_short:
                break
            else:
                is_selected[mini_index] = True
        # 判断是不是全连通的
        result = max(distance)
        if result == sys.maxsize:
            return -1
        else:
            return result


demo = Solution()
print(demo.networkDelayTime(n=5,
                            times=[[2, 4, 10], [5, 2, 38], [3, 4, 33], [4, 2, 76], [3, 2, 64], [1, 5, 54], [1, 4, 98],
                                   [2, 3, 61], [2, 1, 0], [3, 5, 77], [5, 1, 34], [3, 1, 79], [5, 3, 2], [1, 2, 59],
                                   [4, 3, 46], [5, 4, 44], [2, 5, 89], [4, 5, 21], [1, 3, 86], [4, 1, 95]],
                            k=1))
