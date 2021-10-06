class Solution:
    def toHex(self, num: int) -> str:
        # a = 1 if num > 0 else -1
        # num = abs(num)
        if n == 0:
            return 0
        result = []
        count = 0
        while num != 0 and count < 8:
            c = num & 0xF
            if c == 10:
                c = 'a'
            if c == 11:
                c = 'b'
            if c == 12:
                c = 'c'
            if c == 13:
                c = 'd'
            if c == 14:
                c = 'e'
            if c == 15:
                c = 'f'
            result.append(str(c))
            num >>= 4
            count += 1
        result.reverse()
        # if a == -1:
        #     return '-' + ''.join(result)
        # else:
        return ''.join(result)

demo = Solution()
print(demo.toHex(26))
print(demo.toHex(-1))