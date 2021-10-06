from collections import Counter, defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        使用counter记录出了每个数字的出现频率
        三个大于0的数与三个小于0的数相加肯定不能在一起
        :param nums:
        :return:
        """
        d = defaultdict(int)
        big_zero = []
        small_zero = []
        result = []
        for i in range(len(nums)):
            d[nums[i]] += 1
        for i in d.keys():
            if i >= 0:
                big_zero.append(i)
            else:
                small_zero.append(i)
        big_zero.sort()
        small_zero.sort()
        m = len(big_zero)
        n = len(small_zero)
        for i in range(m):
            for j in range(i, m):
                a = big_zero[i]
                b = big_zero[j]
                c = -(a + b)
                if a != b != c:
                    if d[c] > 0 and d[a] > 0 and d[b] > 0:
                        # z = min(d[a], d[b], d[c])
                        # d[a] -= z
                        # d[b] -= z
                        # d[c] -= z
                        result.append([a, b, c])
                elif a == b == c:
                    if d[a] > 2:
                        result.append([a, b, c])
                else:
                    if a == b:
                        if d[c] > 0 and d[b] > 1:
                            # z = min(d[a] // 2, d[c])
                            # d[a] -= 2 * z
                            # d[c] -= z
                            result.append([a, b, c])
                    elif b == c:
                        if d[a] > 0 and d[c] > 1:
                            # z = min(d[c] // 2, d[a])
                            # d[c] -= 2 * z
                            # d[a] -= z
                            result.append([a, b, c])
                    elif a == c:
                        if d[b] > 0 and d[c] > 1:
                            # z = min(d[c] // 2, d[b])
                            # d[c] -= 2 * z
                            # d[b] -= z
                            result.append([a, b, c])
                # if d[a] <= 0:
                #     continue
        for i in range(n):
            for j in range(i, n):
                a = small_zero[i]
                b = small_zero[j]
                c = -(a + b)
                if a != b != c:
                    if d[c] > 0 and d[a] > 0 and d[b] > 0:
                        # z = min(d[a], d[b], d[c])
                        # d[a] -= z
                        # d[b] -= z
                        # d[c] -= z
                        result.append([a, b, c])
                elif a == b == c:
                    if d[a] > 2:
                        result.append([a, b, c])
                else:
                    if a == b:
                        if d[c] > 0 and d[b] > 1:
                            # z = min(d[a] // 2, d[c])
                            # d[a] -= 2 * z
                            # d[c] -= z
                            result.append([a, b, c])
                    elif b == c:
                        if d[a] > 0 and d[c] > 1:
                            # z = min(d[c] // 2, d[a])
                            # d[c] -= 2 * z
                            # d[a] -= z
                            result.append([a, b, c])
                    elif a == c:
                        if d[b] > 0 and d[c] > 1:
                            # z = min(d[c] // 2, d[b])
                            # d[c] -= 2 * z
                            # d[b] -= z
                            result.append([a, b, c])
                # if d[a] <= 0:
                #     continue
        return result


demo = Solution()
print(demo.threeSum([-1, 0, 1, 2, -1, -4]))
