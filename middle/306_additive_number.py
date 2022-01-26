"""
每一个数 都是逐渐增大的（除了最开始两个数，但是最开始两个数也都是正数）
困难也就变成了 如何选取开头两个数字
每个数字没有前置0
第二个数字为一位，第一个数字也为一位
除了最开始两个数，其他数都是等于它之前两个数相加的和
"""


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        """
        zero 第一个数的位数
        one 第二个数的位数
        """
        def is_equal(zero: int, one: int) -> bool:
            f = 0
            while True:
                a = num[f:zero]
                b = num[zero:one]
                if a[0] == '0' and a != ''.join('0'*len(a)):
                    return False
                if b[0] == '0' and b != ''.join('0'*len(b)):
                    return False
                carry = 0
                c = ''
                # if num[one] == '0':
                    # return False
                for jk in range(min(len(a), len(b))):
                    z = int(a[-jk - 1]) + int(b[-jk - 1]) + carry
                    if z >= 10:
                        carry = 1
                        c += str(z - 10)
                    else:
                        c += str(z)
                        carry = 0
                if len(a) > len(b):
                    for kl in range(min(len(a), len(b)), len(a)):
                        z = int(a[-kl-1]) + carry
                        if z >= 10:
                            carry = 1
                            c += str(z-10)
                        else:
                            c += str(z)
                            carry = 0
                elif len(b) > len(a):
                    for kl in range(min(len(a), len(b)), len(b)):
                        z = int(b[-kl - 1]) + carry
                        if z >= 10:
                            carry = 1
                            c += str(z - 10)
                        else:
                            c += str(z)
                            carry = 0
                if carry == 1:
                    c += '1'
                c = c[::-1]
                if len(c)+one > len(num):
                    return False
                if c != num[one:one+len(c)]:
                    return False
                if c == num[one:one+len(c)] and len(c)+one == len(num):
                    # print("c:{0},a:{1},b:{2}".format(c,a,b))
                    return True
                f = zero
                zero = one
                one = one + len(c)
        if len(num)<=2:
            return False
        for i in range(1, len(num) // 2+1):
            # 这里应该还要加一个第二个数的位数，弟二个数的位数可以不一定
            for j in range(1, (len(num)-i)//2+1):
                a = num[0:i]
                b = num[i:i+j]
                if a[0] == '0' and a != ''.join('0' * len(a)):
                    break
                if b[0] == '0' and b != ''.join('0' * len(b)):
                    break
                if is_equal(i,i+j):
                    return True
        return False
demo = Solution()
print(demo.isAdditiveNumber("199001200"))
print(demo.isAdditiveNumber('199111992'))
print(demo.isAdditiveNumber('211738'))
print(demo.isAdditiveNumber("000"))