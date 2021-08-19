# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
from math import sqrt


class Solution:
    def countDigitOne(self, n: int) -> int:
        l = [0]
        temp = n
        data = temp
        num = 1
        data_arr = []
        count = 0
        while data > 0:
            l.append(num)
            data_arr.append(data%10)
            num = num*10 + pow(10,len(l)-1)
            data = int(data /10)
        for i in range(len(data_arr)):
            # if data_arr[i] == 0:
            #     if data > 0:
            #         count += data
            if data_arr[i] == 1:
                count += l[i] + (data+1)
            elif data_arr[i] > 0:
                count += l[i]*data_arr[i] + pow(10, i)
            if i >= 1:
                data = data + data_arr[i] * pow(10, i)
            elif i == 0:
                data = data_arr[i]
        return count


demo =Solution()
print(demo.countDigitOne(98076))