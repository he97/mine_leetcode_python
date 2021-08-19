# 给你两个字符串 s 和 p ，其中 p 是 s 的一个 子序列 。
# 同时，给你一个元素 互不相同 且下标 从 0 开始 计数的整数数组removable ，
# 该数组是 s 中下标的一个子集（s 的下标也 从 0 开始 计数）。
#
# 请你找出一个整数 k（0 <= k <= removable.length），
# 选出removable 中的 前 k 个下标，
# 然后从 s 中移除这些下标对应的 k 个字符。
# 整数 k 需满足：
# 在执行完上述步骤后， p 仍然是 s 的一个 子序列 。
# 更正式的解释是，对于每个 0 <= i < k ，先标记出位于 s[removable[i]] 的字符，
# 接着移除所有标记过的字符，然后检查 p 是否仍然是 s 的一个子序列。
#
# 返回你可以找出的 最大 k ，满足在移除字符后 p 仍然是 s 的一个子序列。
#
# 字符串的一个 子序列 是一个由原字符串生成的新字符串，
# 生成过程中可能会移除原字符串中的一些字符（也可能不移除）
# 但不改变剩余字符之间的相对顺序。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-number-of-removable-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    # 二分法
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        low = 0
        high = len(removable)
        list_s = list(s)
        list_p = list(p)
        mid = 0
        temp = []
        while low <= high:
            temp = list_s.copy()
            mid = int((low + high) / 2)
            for i in range(0, mid):
                temp[removable[i]] = 'A'
            i_index = j_index = 0
            while i_index < len(temp) and j_index < len(list_p):
                if temp[i_index] == list_p[j_index]:
                    i_index += 1
                    j_index += 1
                else:
                    i_index += 1
            #         是子序列
            if j_index == len(list_p) and i_index <= len(temp):
                low = mid + 1
            elif i_index == len(temp) and j_index < len(list_p):
                high = mid - 1
        return low - 1



demo = Solution()
print(demo.maximumRemovals("abcacb"
,"ab"
,[3,1,0]))
print(demo.maximumRemovals("qobftgcueho"
                           , "obue"
                           , [5, 3, 0, 6, 4, 9, 10, 7, 2, 8]))
print(demo.maximumRemovals("abcacb", "ab", [3, 1, 0]))
print(demo.maximumRemovals(s="abcbddddd", p="abcd", removable=[3, 2, 1, 4, 5, 6]))
print(demo.maximumRemovals(s="abcab", p="abc", removable=[0, 1, 2, 3, 4]))
