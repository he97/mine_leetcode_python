# 你和你的朋友，两个人一起玩Nim 游戏：
#
# 桌子上有一堆石头。
# 你们轮流进行自己的回合，你作为先手。
# 每一回合，轮到的人拿掉1 - 3 块石头。
# 拿掉最后一块石头的人就是获胜者。
# 假设你们每一步都是最优解。请编写一个函数，来判断你是否可以在给定石头数量为 n 的情况下赢得游戏。如果可以赢，返回 true；否则，返回 false 。
#
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/nim-game
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def canWinNim(self, n: int) -> bool:
        m = n % 4
        if m == 0:
            return False
        else:
            return True
        # dp = [False for _ in range(n+1)]
        # for i in range(1, 4):
        #     if i <= n:
        #         dp[i] = True
        # index = 4
        # while index <= n:
        #     # 到个一到三
        #     # 自己先取三个数 如果取得一个数的所有情况都能成功 那么自己就能成功
        #     for i in range(1,4):
        #         tag = True
        #         # 对手再取三个数
        #         for j in range(1, 4):
        #             if index - i - j <= 0:
        #                 tag = False
        #                 break
        #             else:
        #                 if not dp[index - i - j]:
        #                     tag = False
        #                     break
        #         if tag:
        #             dp[index] = True
        #             break
        #     index += 1
        # return dp[n]

demo = Solution()
for i in range(120):
    print(demo.canWinNim(i))