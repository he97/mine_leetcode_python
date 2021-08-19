# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
#
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列
from collections import defaultdict


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        chars = list(s)
        n = len(chars)
        dp = [[0 for _ in chars]for _ in chars]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-2,-1,-1):
            for j in range(i+1, n):
                if chars[i] == chars[j]:
                    dp[i][j] = 2+dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]


demo = Solution()
print(demo.longestPalindromeSubseq("abcabcabc"))
print(demo.longestPalindromeSubseq("bbbab"))
