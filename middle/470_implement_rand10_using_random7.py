# The rand7() API is already defined for you.
import math
import random


def rand7():
    return random.randint(1,7)


# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        first = 0
        while True:
            a = rand7()
            if a <= 5:
                first = a
                break
        while True:
            b = rand7()
            if b != 4:
                if b <= 3:
                    return 2 * first - 1
                elif b >= 5:
                    return 2 * first

demo = Solution()
n = 10000
c = [0 for _ in range(11)]
for i in range(n):
    a = demo.rand10()
    c[a] += 1
print(c)
