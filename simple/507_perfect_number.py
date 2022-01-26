# 对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。
#
# 给定一个 整数 n， 如果是完美数，返回 true，否则返回 false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/perfect-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
使用单层循环吗，有没有更高效的方式呢？
正因子，是不是可以找到质因子，再用质因子相乘得到呢？不知道
下面写的是单层循环
"""
from collections import defaultdict


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        d = [0 for _ in range(num)]
        ans = 0
        for i in range(1, num // 2 + 1):
            if d[i] == 0:
                a = int(num / i)
                if num % i == 0:
                    d[i] += 1
                    d[a] += 1
                    ans += i+a
        if ans == num:
            return True
        else:
            return False

