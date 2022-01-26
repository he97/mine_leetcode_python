# 给你一个非常大的整数 n 和一个整数数字 x ，大整数 n 用一个字符串表示。n 中每一位数字和数字 x 都处于闭区间 [1, 9] 中，且 n 可能表示一个 负数 。
#
# 你打算通过在 n 的十进制表示的任意位置插入 x 来 最大化 n 的 数值 ​​​​​​。但 不能 在负号的左边插入 x 。
#
# 例如，如果 n = 73 且 x = 6 ，那么最佳方案是将 6 插入 7 和 3 之间，使 n = 763 。
# 如果 n = -55 且 x = 2 ，那么最佳方案是将 2 插在第一个 5 之前，使 n = -255 。
# 返回插入操作后，用字符串表示的 n 的最大值。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-value-after-insertion
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
对于正数，在第一个小于插入的数的数之前插入
对于负数，在第一个大于插入的数的数之前插入
"""


class Solution:
    def maxValue(self, n: str, x: int) -> str:
        l = list(n)
        s = ''
        # upper 0
        if l[0] != '-':
            for i in range(0, len(l)):
                if int(l[i]) <= x:
                    s = ''.join(l[0:i])
                    s += str(x)
                    s += ''.join((l[i:]))
                    break
        # below zero
        else:
            for i in range(1, len(l)):
                if int(l[i]) >= x:
                    s = ''.join(l[0:i])
                    s += str(x)
                    s += ''.join((l[i:]))
                    break
        return s
