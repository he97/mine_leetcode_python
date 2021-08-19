# 超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。
#
# 给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。
#
# 题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/super-ugly-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 输入：n = 12, primes = [2,7,13,19]
# 输出：32
# 解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/super-ugly-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import sys
from typing import List

# 动态规划求解
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        prime_index = []
        result = [1]
        for i in range(len(primes)):
            prime_index.append(0)
        while True:
            min_multi = sys.maxsize
            min_index = 0
            for i in range(len(primes)):
                if primes[i] * result[prime_index[i]] < min_multi:
                    min_multi = primes[i] * result[prime_index[i]]
                    min_index = i
            if result[-1] < min_multi:
                result.append(min_multi)
            prime_index[min_index] += 1
            if len(result) >= n:
                return result[n-1]


demo = Solution()
# print(demo.nthSuperUglyNumber(n=12, primes=[2, 7, 13, 19]))
print(demo.nthSuperUglyNumber(n=1, primes=[2,3,5]))
