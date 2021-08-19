# 假设有从 1 到 N 的 N 个整数，
# 如果从这 N 个数字中成功构造出一个数组，
# 使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，
# 我们就称这个数组为一个优美的排列。条件：
# 
# 第 i 位的数字能被 i 整除
# i 能被第 i 位上的数字整除
# 现在给定一个整数 N，请问可以构造多少个优美的排列？
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/beautiful-arrangement
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from collections import defaultdict


class Solution:
    def countArrangement(self, n: int) -> int:
        f = [0] * (1 << n)
        f[0] = 1
        for mask in range(1, 1 << n):
            num = bin(mask).count("1")
            for i in range(n):
                if mask & (1 << i) and (num % (i + 1) == 0 or (i + 1) % num == 0):
                    f[mask] += f[mask ^ (1 << i)]

        return f[(1 << n) - 1]

# class Solution:
    # def countArrangement(self, n: int) -> int:
    #     d = defaultdict(int)
    #     for i in range(1, n + 1):
    #         d[i] = True
    #
    #     def get_count(index: int, dd) -> int:
    #         j = 1
    #         count = 0
    #         if index == n:
    #             while j <= n:
    #                 if dd[j] and (index % j == 0 or j % index == 0):
    #                     count += 1
    #                 j += 1
    #             return count
    #         while j <= n:
    #             if dd[j] and (index % j == 0 or j % index == 0):
    #                 dd[j] = False
    #                 count += get_count(index + 1, dd)
    #                 dd[j] = True
    #             j += 1
    #         return count
    #
    #     return get_count(1, d)


demo = Solution()
print(demo.countArrangement(2))
