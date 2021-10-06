# You are given a string s consisting only of characters 'a' and 'b'​​​​.
#
# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
#
# Return the minimum number of deletions needed to make s balanced.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-deletions-to-make-string-balanced
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

# 以下方法时间消耗过高
# 学习动态规划再来吧
class Solution:
    def minimumDeletions(self, s: str) -> int:
        l = list(s)
        dp = [0] * len(l)
        illegal_b = 0
        tag_a = tag_b = False
        for i in range(len(l)):
            if i == 0:
                if l[i] == 'a':
                    dp[0] = 0
                    tag_a = True
                else:
                    dp[0] = 0
                    tag_b = True
            if l[i] == 'a':
                if not tag_a:
                    tag_a = True
                if not tag_b:
                    dp[i] = dp[i-1]
                else:
                    if dp[i-1]+1 < illegal_b:
                        dp[i] = dp[i - 1] + 1
                    else:
                        dp[i] = illegal_b
            elif l[i] == 'b':
                if not tag_a:
                    dp[i] = dp[i-1]
                illegal_b += 1
                if not tag_b:
                    tag_b = True
                dp[i] = dp[i-1]
        return dp[-1]





demo = Solution()
result = demo.minimumDeletions(s="aaaaaabbbbabaaaabbabaaabbabbbaaabababaaaaaaabbaaabaaababaaabababa")
print(result)
