"""
假设五位数
00000 00001 00011 00111 01111 11111 10111 10011 10001 100000
三位数呢 000 尾部的是 001 010 100 三种
 001 011 111 110 100 101
 0 1 //n=1
 00 01 11 10//n =2
 000 001 011 010 110 111 101 100//n=3
 0000 0001 0011 0010 0110 0111 0101 0100 应该这么变换 1100 1101 1111 1110 1010 1011 1001 1000

"""
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        gray_code = [0,1]
        # new = []
        if n == 1:
            return gray_code
        else:
            for i in range(n-1):
                temp = []
                for j in gray_code:
                    temp.append(j)
                for j in reversed(gray_code):
                    temp.append(2**(i+1) + j)
                gray_code = temp
            return gray_code

