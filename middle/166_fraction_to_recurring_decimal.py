class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        small_0 = []
        if numerator * denominator < 0:
            flag = '-'
            numerator = abs(numerator)
            denominator = abs(denominator)
        else:
            flag = ''
        big_0 = numerator // denominator
        remainder = numerator % denominator
        i = 0
        while i < 10000 and remainder != 0:
            remainder = remainder * 10
            c = remainder // denominator
            remainder = remainder % denominator
            small_0.append(str(c))
            i += 1
        a = len(small_0)
        #     从1开始循环
        for i in range(a):
            # if i == 1:
            #     print()
            for j in range(1, ((a-i)//2)+1):
                times = (a-i) // j
                tag = True
                for k in range(1, times):
                    if small_0[i:i+j] != small_0[i + k * j:i + (k+1) * j]:
                        tag = False
                        break
                if tag:
                    return flag + str(big_0) + '.' + ''.join(small_0[0:i]) + '(' + ''.join(small_0[i:i+j]) + ')'
        # interval = 0
        # for i in range(a):
        #     tag = False
        #     end = start = 0
        #     for j in range(1, (a - i) // 2):
        #         if small_0[i:i + j] == small_0[i + j:i + 2 * j]:
        #             if not tag:
        #                 tag = True
        #                 start = i
        #                 end = i + j
        #             else:
        #                 if 0 != j % (end - start):
        #                     start = i
        #                     end = i + j
        #                 else:
        #                     for k in range(1, j // (end - start) + 1):
        #                         if small_0[start:end] != small_0[i + (k - 1) * (end - start):i + k * (end - start)]:
        #                             start = i
        #                             end = i + j
        #                             break
        #     if tag:
        #         return flag + str(big_0) + '.' + ''.join(small_0[0:start]) + '(' + ''.join(small_0[start:end]) + ')'
        # if a >= 2 and small_0[0:a // 2] == small_0[a // 2:]:
        #     return str(big_0) + '.(' + ''.join(small_0[0:a // 2]) + ')'
        if len(small_0) > 0:
            return flag + str(big_0) + '.' + ''.join(small_0)
        else:
            return flag + str(big_0)


demo = Solution()
print(demo.fractionToDecimal(1,6))
print(demo.fractionToDecimal(1, 214748364))
print(demo.fractionToDecimal(-50, 8))
print(demo.fractionToDecimal(1, 333))
print(demo.fractionToDecimal(1, 2))
