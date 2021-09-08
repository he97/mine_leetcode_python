# 假设 力扣（LeetCode）即将开始 IPO 。为了以更高的价格将股票卖给风险投资公司，力扣 希望在 IPO 之前开展一些项目以增加其资本。 由于资源有限，它只能在 IPO 之前完成最多 k 个不同的项目。帮助 力扣 设计完成最多 k 个不同项目后得到最大总资本的方式。
#
# 给你 n 个项目。对于每个项目 i ，它都有一个纯利润 profits[i] ，和启动该项目需要的最小资本 capital[i] 。
#
# 最初，你的资本为 w 。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。
#
# 总而言之，从给定项目中选择 最多 k 个不同项目的列表，以 最大化最终资本 ，并输出最终可获得的最多资本。
#
# 答案保证在 32 位有符号整数范围内。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ipo
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

from sortedcontainers import SortedList


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        d = {}
        n = len(profits)
        count = w
        s = SortedList()
        for i in range(n):
            if capital[i] not in d.keys():
                c = SortedList()
                c.add(profits[i])
                d[capital[i]] = c
            else:
                d[capital[i]].add(profits[i])
        while k > 0:
            if len(d.keys()) > 0:
                for i in sorted(d.keys()):
                    if i <= count:
                        s.update(d[i])
                        d.pop(i)
                    else:
                        break
            if len(s) != 0:
                count += s.pop()
            else:
                return count
            # index = 0
            # maximum = -1
            # tag = False
            # for i in d.keys():
            #     if i <= count:
            #         if d[i][-1] > maximum:
            #             tag = True
            #             maximum = d[i][-1]
            #             index = i
            # if not tag:
            #     return count
            # count += d[index][-1]
            # if len(d[index]) == 1:
            #     d.pop(index)
            # else:
            #     d[index].pop()
            k -= 1
        return count


demo = Solution()
print(demo.findMaximizedCapital(1
                                , 0
                                , [1, 2, 3]
                                , [1, 1, 2]))
print(demo.findMaximizedCapital(k=3, w=0, profits=[1, 2, 3], capital=[0, 1, 2]))
