# 给你 k 枚相同的鸡蛋，
# 并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。
# 
# 已知存在楼层 f ，满足0 <= f <= n ，
# 任何从 高于 f 的楼层落下的鸡蛋都会碎，
# 从 f 楼层或比它低的楼层落下的鸡蛋都不会破。
# 
# 每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下
# （满足1 <= x <= n）。
# 如果鸡蛋碎了，你就不能再次使用它。
# 如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。
# 
# 请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/super-egg-drop
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        memo = {}

        def dp(eggs, level):
            if (eggs, level) not in memo:
                if level == 0:
                    ans = 0
                elif eggs == 1:
                    ans = level
                else:
                    low = 1
                    high = level
                    while low + 1 < high:
                        x = (low + high) // 2
                        t1 = dp(eggs - 1, x - 1)
                        t2 = dp(eggs, level - x)
                        if t1 > t2:
                            high = x
                        elif t1 < t2:
                            low = x
                        else:
                            low = high = x
                    ans = 1 + min(max(dp(eggs - 1, x - 1), dp(eggs, level - x)) for x in (low, high))
                memo[eggs, level] = ans
            return memo[eggs, level]

        return dp(k, n)

# class Solution:
#     def superEggDrop(self, k: int, n: int) -> int:
#         memo = {}
#         def dp(k, n):
#             if (k, n) not in memo:
#                 if n == 0:
#                     ans = 0
#                 elif k == 1:
#                     ans = n
#                 else:
#                     lo, hi = 1, n
#                     # keep a gap of 2 x values to manually check later
#                     while lo + 1 < hi:
#                         x = (lo + hi) // 2
#                         t1 = dp(k - 1, x - 1)
#                         t2 = dp(k, n - x)
#
#                         if t1 < t2:
#                             lo = x
#                         elif t1 > t2:
#                             hi = x
#                         else:
#                             lo = hi = x
#
#                     ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x))
#                                   for x in (lo, hi))
#
#                 memo[k, n] = ans
#             return memo[k, n]
#
#         return dp(k, n)
demo = Solution()
print(demo.superEggDrop(3,14))
