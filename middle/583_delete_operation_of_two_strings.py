# 给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
import pandas as pd
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l_1 = list(word1)
        l_2 = list(word2)
        m = len(l_1)
        n = len(l_2)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        tag = False
        for i in range(n):
            if not tag:
                if l_1[0] == l_2[i]:
                    tag = True
                    dp[0][i] = 1
            else:
                dp[0][i] = 1
        tag = False
        for i in range(m):
            if not tag:
                if l_1[i] == l_2[0]:
                    tag = True
                    dp[i][0] = 1
            else:
                dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                a = 0
                if l_1[i] == l_2[j] and dp[i - 1][j] == dp[i][j-1] == dp[i-1][j-1]:
                    a = 1
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + a
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + a

            # for k in range(i+1, m):
            #     a = 0
            #     if l_1[k] == l_2[i] and dp[k-1][i] == dp[k][i-1]:
            #         a = 1
            #         dp[k][i] = max(dp[k - 1][i], dp[k][i - 1]) + a
            #     else:
            #         dp[k][i] = max(dp[k - 1][i], dp[k][i - 1]) + a

        # df = pd.DataFrame(dp,columns=l_2,index=l_1)
        # df.to_excel('fk.xlsx')
        return m + n - 2 * dp[m - 1][n - 1]


demo = Solution()
print(demo.minDistance("fypcerlwzhpljjjeyktjyyyectnyptshgtzkorvnna"
,"rswjkkcrrwtzfgjrjlbpyiiucvtkxvi"))
print(demo.minDistance("intention"
,"execution"))
print(demo.minDistance("food"
                       , "money"))
print(demo.minDistance(word1="sea", word2="eat"))
print(demo.minDistance(word1="leetcode", word2="etco"))
