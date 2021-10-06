from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        m = len(cuts)
        dp = [[0 for _ in range(n)] for _ in range(m+2)]
        cuts = [0] + sorted(cuts) + [n]
        for i in range(m,0,-1):
            for j in range(i,m+1):
                interval = i
                b = interval + j
                if b < n:
                    ans = float('inf')
                    count = 0
                    for k in cuts:
                        if j < k < b:
                            count += 1
                            ans = min(dp[j][k]+dp[k][b],ans)
                    if ans == float('inf'):
                        dp[j][b] = (b-j)
                    else:
                        # dp[j][b] = ans + (b - j)
                        if count > 1:
                            dp[j][b] = ans + (b - j)
                        else:
                            dp[j][b] = ans
        return dp[0][n - 1]

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        m = len(cuts)
        cuts = [0] + sorted(cuts) + [n]
        f = [[0] * (m + 2) for _ in range(m + 2)]

        for i in range(m, 0, -1):
            for j in range(i, m + 1):
                f[i][j] = 0 if i == j else \
                    min(f[i][k - 1] + f[k + 1][j] for k in range(i, j + 1))
                f[i][j] += cuts[j + 1] - cuts[i - 1]

        return f[1][m]

demo = Solution()
print(demo.minCost(n=9, cuts=[5, 6, 1, 4, 2]))
print(demo.minCost(n=7, cuts=[1, 3, 4, 5]))

