# 给你一个长度为 n 的字符串 s ，和一个整数 k 。请你找出字符串 s 中 重复 k 次的 最长子序列 。
#
# 子序列 是由其他字符串删除某些（或不删除）字符派生而来的一个字符串。
#
# 如果seq * k 是 s 的一个子序列，其中 seq * k 表示一个由 seq 串联 k次构造的字符串，那么就称 seq 是字符串 s 中一个 重复 k 次 的子序列。
#
# 举个例子，"bba" 是字符串 "bababcba" 中的一个重复 2 次的子序列，因为字符串 "bbabba" 是由 "bba" 串联 2 次构造的，而"bbabba" 是字符串 "bababcba" 的一个子序列。
# 返回字符串 s 中 重复 k 次的最长子序列 。如果存在多个满足的子序列，则返回 字典序最大 的那个。如果不存在这样的子序列，返回一个 空 字符串
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-subsequence-repeated-k-times
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import copy
import math
from collections import defaultdict, Counter
from itertools import combinations, permutations


# class Solution:
#     def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
#         l = list(s)
#         n = len(l)
#         m = math.floor(n / k)
#         c = [[i] for i in range(n)]
#         pre = ''
#         le = 1
#         while len(c) > 0 and le <= m:
#             arr = []
#             result = []
#             length = len(c[0])
#             for i in c:
#                 tag = False
#                 index = 0
#                 index_2 = i[-1] + 1
#                 temp = k - 1
#                 while temp > 0:
#                     while index < length and index_2 < n:
#                         if l[i[index]] == l[index_2]:
#                             if index == length - 1:
#                                 if temp == 1:
#                                     tag = True
#                                     break
#                                 temp -= 1
#                                 index = 0
#                                 index_2 += 1
#                                 continue
#                             index += 1
#                             index_2 += 1
#                         else:
#                             index_2 += 1
#                     break
#                 if tag:
#                     v = ''.join([str(l[_]) for _ in i])
#                     result.append(v)
#                     u = i
#                     for h in range(u[-1]+1, n):
#                         u.append(h)
#                         arr.append(copy.deepcopy(u))
#                         u.pop()
#             c = arr
#             if len(arr) > 0:
#                 pre = max(result)
#         return pre

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        num = Counter(s)
        # ele * (num[ele] // k 表明了这个单词最多可以出现多少次 如 4//2 = 2 就说明可以出现两次
        hot = ''.join(ele * (num[ele] // k) for ele in sorted(num, reverse=True))
        for i in range(len(hot), 0, -1):
            for item in permutations(hot, i):
                word = ''.join(item)
                ss = iter(s)
                # *k 是为了保证循环n次，确保单词出现了n次
                if all(c in ss for c in word * k):
                    return word
        return ''


demo = Solution()
print(demo.longestSubsequenceRepeatedK(s="letsleetcode", k=2))
#         for k in range(j[-1]+1, n):
#             if [index] ==
# combinations
