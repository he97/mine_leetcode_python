# 一条包含字母A-Z 的消息通过以下的方式进行了编码：
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 要 解码 一条已编码的消息，所有的数字都必须分组，然后按原来的编码方案反向映射回字母（可能存在多种方式）。例如，"11106" 可以映射为：
#
# "AAJF" 对应分组 (1 1 10 6)
# "KJF" 对应分组 (11 10 6)
# 注意，像 (1 11 06) 这样的分组是无效的，因为 "06" 不可以映射为 'F' ，因为 "6" 与 "06" 不同。
#
# 除了 上面描述的数字字母映射方案，编码消息中可能包含 '*' 字符，可以表示从 '1' 到 '9' 的任一数字（不包括 '0'）。例如，编码字符串 "1*" 可以表示 "11"、"12"、"13"、"14"、"15"、"16"、"17"、"18" 或 "19" 中的任意一条消息。对 "1*" 进行解码，相当于解码该字符串可以表示的任何编码消息。
#
# 给你一个字符串 s ，由数字和 '*' 字符组成，返回 解码 该字符串的方法 数目 。
#
# 由于答案数目可能非常大，返回对 109 + 7 取余 的结果。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-ways-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def numDecodings(self, s: str) -> int:
        l = list(s)
        n = len(l)
        for i in range(n):
            if l[i] != '*':
                if 0 <= int(l[i]) <= 9:
                    l[i] = int(l[i])
        dp = [0] * n
        d = [0] * n
        if l[0] == '*':
            dp[0] = 9
        elif l[0] == 0:
            return 0
        elif 0 < l[0] <= 9:
            dp[0] = 1
        for i in range(1, n):
            count = 0
            if l[i] == '*':
                count += dp[i - 1] * 9
                if l[i - 1] == 1:
                    if i == 1:
                        count += 9
                    else:
                        count += dp[i - 2] * 9
                elif l[i - 1] == 2:
                    if i == 1:
                        count += 6
                    else:
                        count += dp[i - 2] * 6
                elif l[i - 1] == '*':
                    if i == 1:
                        count += 15
                    else:
                        count += dp[i - 2] * 15
                dp[i] = count % (10**9+7)
            # 当前数字为0
            elif l[i] == 0:
                if l[i - 1] == '*':
                    if i == 1:
                        dp[i] = 2
                    else:
                        dp[i] = (dp[i - 2] * 2) % (10**9+7)
                elif 3 <= l[i - 1] <= 9 or l[i - 1] == 0:
                    return 0
                elif 1 <= l[i - 1] <= 2:
                    if i == 1:
                        dp[i] = 1
                    else:
                        dp[i] = (dp[i - 2]) % (10**9+7)
            elif 0 < l[i] <= 6:
                count += dp[i - 1]
                if l[i - 1] == '*':
                    if i == 1:
                        count += 2
                    else:
                        count += dp[i-2]*2
                elif l[i - 1] == 1 or l[i - 1] == 2:
                    if i == 1:
                        count += 1
                    else:
                        count += dp[i-2]
                dp[i] = count % (10**9+7)
            elif 7 <= l[i] <= 9:
                count += dp[i - 1]
                if l[i - 1] == '*' or l[i - 1] == 1:
                    if i == 1:
                        count += 1
                    else:
                        count += dp[i - 2]
                dp[i] = count % (10**9+7)
        return dp[-1] % (10**9+7)
demo = Solution()
print(demo.numDecodings("*1*1*0"))
print(demo.numDecodings("1*2"))