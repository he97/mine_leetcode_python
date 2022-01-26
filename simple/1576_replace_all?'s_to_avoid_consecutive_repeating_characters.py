# 给你一个仅包含小写英文字母和 '?' 字符的字符串 s，请你将所有的 '?' 转换为若干小写字母，使最终的字符串不包含任何 连续重复 的字符。
#
# 注意：你 不能 修改非 '?' 字符。
#
# 题目测试用例保证 除 '?' 字符 之外，不存在连续重复的字符。
#
# 在完成所有转换（可能无需转换）后返回最终的字符串。如果有多个解决方案，请返回其中任何一个。可以证明，在给定的约束条件下，答案总是存在的。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
ord()是转化为ascii码
chr()是ascii转字符
"""
from collections import defaultdict, Counter
print('zzzz')


class Solution:
    def modifyString(self, s: str) -> str:
        # d = Counter(ord(s[i]) - 97 for i in range(len(s)))
        # print(d)
        s = 'x' + s
        s += 'x'
        for i in range(1, len(s) - 1):
            if s[i] == '?':
                x = 0
                for x in range(26):
                    if ord(s[i - 1]) != 97 + x and ord(s[i + 1]) != 97 + x:
                        s = s.replace('?', chr(97 + x), 1)
                        break
                    x += 1
        s = s[1:len(s) - 1]
        return s


demo = Solution()
demo.modifyString(s="j?qg??b")
