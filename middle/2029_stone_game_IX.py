"""
每个数字，除以三之后，只有 1 2 0三种结果

"""
import collections
from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        z = [x % 3 for x in stones]
        d = collections.Counter(z)
        # z = min(d[1], d[2])
        d[0] %= 2
        # d[1] -= z
        # d[2] -= z
        z = sum(i * d[i] for i in d.keys())
        nodes = sum(d[i] for i in d.keys())
        # 定义一个状态
        tag = True
        while z > 0:
            if z %3 == 0:
                if nodes == 0:

            elif z %3 == 1:

            elif z %3 == 2:

        if d[0] == 0:
            if d[1] == d[2] == 0:
                return True
            if d[1] != 0 or d[2] != 0:
                return True
        elif d[0] == 1:
            if d[1] == 0 and d[2] == 0:
                return False
            if d[1] != 0 or d[2] != 0:
                return True

