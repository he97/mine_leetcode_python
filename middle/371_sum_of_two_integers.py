class Solution:
    def getSum(self, a: int, b: int) -> int:
        temp_a = a
        temp_b = b
        carry_bit = 0
        result = 0
        char_a = a >> 10
        char_b = b >> 10
        m = a.bit_length()
        n = b.bit_length()
        print('a:',bin(a))
        print('b',bin(b))
        tag = False
        for i in range(max(m, n)):
            c = a & 1
            d = b & 1
            if carry_bit == 1:
                if c == d == 1:
                    this = 1
                    carry_bit = 1
                elif c == 1 or d == 1:
                    this = 0
                    carry_bit = 1
                else:
                    this = 1
                    carry_bit = 0
            else:
                if c == d == 1:
                    this = 0
                    carry_bit = 1
                elif c == 1 or d == 1:
                    this = 1
                    carry_bit = 0
                else:
                    this = 0
                    carry_bit = 0
            # print('this:', this)
            if result == 0 and this == 0:
                this = 1
                tag = True
            result = result | this
            result = result << 1
            a = a >> 1
            b = b >> 1
        print('result:', bin(result))
        if carry_bit == 1:
            if char_a == -1:
                if char_b == -1:
                    result |= 1
                else:
                    result |= 0
            else:
                if char_b == -1:
                    result |= 0
                else:
                    result |= 1
        else:
            if char_a == -1:
                if char_b == -1:
                    result |= 0
                else:
                    result |= 1
            else:
                if char_b == -1:
                    result |= 1
                else:
                    result |= 0
        # print(bin(result))
        z = 0
        while result != 0:
            c = result & 1
            z = z | c
            z <<= 1
            result >>= 1
        z >>= 1
        if tag:
            z >>= 1
            z <<= 1
            z |= 0
        # print('z:{0},bin(z):{1}'.format(z,bin(z)))
        # print('a:{0},b:{0}'.format(a,b))
        if (min(temp_a, temp_b) < 0 and abs(max(temp_a, temp_b)) < abs(min(temp_a, temp_b))) or (temp_a < 0 and temp_b < 0):
            x = 0
            b = 1
            while z != 0:
                c = z & 1
                if b == 1:
                    if c == 1:
                        c = 0
                        b = 0
                    elif c == 0:
                        c = 1
                        b = 1
                # print('更改前x:', bin(x))
                if c == 0:
                    c = 1
                elif c == 1:
                    c = 0
                x |= c
                x <<= 1
                z >>= 1
                # print('x:',bin(x))
            z = 0
            while x != 0:
                c = x & 1
                # print('更改前x:', bin(x))
                if c == 0 and z == 0:
                    x >>= 1
                    continue
                z |= c
                x >>= 1
                z <<= 1
            z >>= 1
            # print('z:', bin(z))
            z = -z
            # print('z:', bin(z))
        # print('bin(101):', bin(-101))
        return z


demo = Solution()
print(demo.getSum(-12,-8))
print(demo.getSum(20,30))
print(demo.getSum(a=2, b=3))
print(demo.getSum(100, -5))
print(demo.getSum(100, 1))
print(demo.getSum(-100, -1))
print(demo.getSum(-100, -5))
print(demo.getSum(-100, 5))
print(demo.getSum(100, -100))
print(demo.getSum(445, -6))
