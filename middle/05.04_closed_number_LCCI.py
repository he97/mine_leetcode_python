# 下一个数。给定一个正整数，找出与其二进制表达式中1的个数相同且大小最接近的那两个数（一个略大，一个略小）。
from typing import List


class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        index_1 = -1
        index_1_2 = -1
        index_0 = -1
        count_1 = 0
        count_0 = 0
        count = 0
        tem = 0
        a = -1
        a_tag = False
        b = -1
        b_tag = False
        c = 1
        n = num
        data = []
        while n > 0:
            data.append(n % 2)
            n = int(n / 2)
        m = len(data)
        i = 0
        while data[i] != 1 and i < m:
            count_0 += 1
            i += 1
        index_1 = i
        while i < m and data[i] != 0:
            tem += 2 ** i
            count_1 += 1
            i += 1
        #     如果是全1
        if i == m:
            if index_1 == 0:
                if num - 2 ** (i - 1) + 2 ** i < 2**31:
                    return [num - 2 ** (i - 1) + 2 ** i, -1]
                else:
                    return [-1,-1]
            else:
                big = 2**m
                for k in range(count_1 - 1):
                    big += 2 ** k
                small = num - 2 ** index_1 + 2**(index_1-1)

                return [big, small]
        else:
            index_0 = i
        while data[i] != 1 and i < m:
            i += 1
        index_1_2 = i
        big = num - tem + 2 ** index_0
        for k in range(count_1 - 1):
            big += 2 ** k
        if count_0 > 0:
            small = num - 2**index_1 + 2**(index_1-1)
        else:
            small = num - 2 ** index_1_2 - tem
            for k in range(count_1 + 1):
                small += 2 ** (index_1_2 - 1 - k)
        return [big, small]

demo = Solution()
print(demo.findClosedNumbers(2147483647))
print(demo.findClosedNumbers(10000))
print(demo.findClosedNumbers(31))
print(demo.findClosedNumbers(34))
print(demo.findClosedNumbers(56))
print(demo.findClosedNumbers(248))
print(demo.findClosedNumbers(411))
print(demo.findClosedNumbers(4518423641))
