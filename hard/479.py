import math


class Solution:
    def largestPalindrome(self, n: int) -> int:
        def check(a:list) -> bool:
            value = 0
            for x in a:
                value*=10
                value+=x
            max_value = 10**n-1
            if value == 0:
                return False
            for x in range(max_value,0,-1):
                if value // x > max_value:
                    return False
                if value % x == 0:
                    print(value)
                    return True
        length = 2*n
        # 如何表示偶数位的回文整数以及表示奇数位的回文整数
        while length > 0:
            print('len:',length)
            a = [9 for _ in range(length)]
            index_value = 9
            index = math.ceil(length / 2)-1
            print('index:',index)
            while a[0] >= 1:
                while a[index] > 0:

                    a[index] = index_value
                    a[-1-index] = index_value
                    print('1,a', a)
                    if check(a):
                        v = 0
                        for x in a:
                            v*=10
                            v+=x
                        return v % 1337
                    else:
                        index_value -= 1
                for i in range(index-1,-1,-1):
                    if a[i] > 0:
                        a[i] -= 1
                        a[-1-i] -= 1
                        for x in range(i+1,length-i-1):
                            a[x] = 9
                        print('2,a',a)
                        index_value = 9
                        break
            length -= 1

demo = Solution()
for x in [8]:
    print(demo.largestPalindrome(x))