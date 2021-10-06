import random
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        x = sum(rolls)
        s = mean * (n + len(rolls))
        m = s - x
        result = []
        if not n <= m <= 6 * n:
            return result
        for i in range(n - 1):
            a = random.randint(1,6)
            # 这块有问题吧？纯属侥幸
            while not ((n - i-1) <= m - a <= 6 * (n - i-1)):
                a = random.randint(1,6)
            m -= a
            result.append(a)
        result.append(m)
        return result

demo = Solution()
print(demo.missingRolls([3,2,4,3]
,4
,2))