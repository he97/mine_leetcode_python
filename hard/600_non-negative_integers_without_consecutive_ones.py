# 给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。
from collections import defaultdict


class Solution:
    def findIntegers(self, n: int) -> int:
        temp = n
        data = []
        index = 0
        count = 0
        while temp > 0:
            data.append(temp % 2)
            index += 1
            temp = int(temp / 2)
        data.reverse()
        d = [0 for _ in range(index + 1)]
        if index >= 1:
            d[1] = 2
        if index >= 2:
            d[2] = 1
        for i in range(3, index+1):
            d[i] = sum(d[1:i-1])
        tag = False
        prev = index
        for i in range(index):
            if data[i] == 1:
                if not tag:
                    tag = True
                    prev = index - i
                else:
                    count += sum(d[1:prev+1])
                    tag = False
                    break
            else:
                if tag:
                    tag = False
                    count += sum(d[1:prev])
                    prev = 0
        if prev == 0:
            count += 1
        if tag:
            count += sum(d[1:prev+1])



        return count



demo = Solution()
# print(demo.findIntegers(52))
print(demo.findIntegers(3))
print(demo.findIntegers(1))
print(demo.findIntegers(5))