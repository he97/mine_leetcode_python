# 给你一个字符串 s和一个整数 k。请你用 s字符串中 所有字符构造 k个非空 回文串。
#
# 如果你可以用s中所有字符构造k个回文字符串，那么请你返回 True，否则返回False。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/construct-k-palindrome-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import math
from collections import defaultdict


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        l = list(s)
        d = {}
        odd = 0
        even = 0
        for i in l:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        for j in d.keys():
            a = math.floor(d[j] / 2)
            b = d[j] % 2
            odd += b
            even += a
        while even >= 0:
            if odd > k:
                return False
            elif even >= k:
                return True
            elif even + odd >= k:
                return True
            even -= 1
            odd += 2
        return False
