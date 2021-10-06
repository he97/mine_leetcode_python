import math
from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        """
        差分数组应该是错的
        每次的传递 选一部分
        相邻的 有可能是左边 也有可能是右边 怎么选择呢
        前面有 就选离前面最近的 后面有 就选离后面最近的
        目的就是一次性使最多的衣服从超过的到不足的洗衣机里
        遍历方向的改变 改为从两边到中间


        最后版本 错的太离谱了
        贪心算法的思想完全错了
        :param machines:
        :return:
        """
        n = sum(machines)
        a = math.floor(n / len(machines))
        b = n % len(machines)
        ans = 0
        if b != 0:
            return -1
        count = 0
        for i in range(len(machines)):
            machines[i] = machines[i] - a
        for i in range(len(machines)):
            count += machines[i]
            ans = min(ans,abs(count),machines[i])
        return ans


demo = Solution()
print(demo.findMinMoves([50,62,75,31,2,84,20,74,49,73]))
print(demo.findMinMoves([0,0,11,0,11,0,0,2]))
print(demo.findMinMoves([0,0,10,0,0,0,10,0,0,0]))
print(demo.findMinMoves([0,0,11,5]))
print(demo.findMinMoves([1,0,5,5,3,2,1,4,5,6,4,2,2,1,4]))
print(demo.findMinMoves([1,0,5]))
print(demo.findMinMoves([0,3,0]))
print(demo.findMinMoves([0,2,0]))