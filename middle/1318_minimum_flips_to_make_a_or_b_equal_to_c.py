# 给你三个正整数a、b 和 c。
# 
# 你可以对 a 和 b的二进制表示进行位翻转操作，
# 返回能够使按位或运算 a OR b == c成立的最小翻转次数。
# 
# 「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0
# 或者 0 变成 1 。
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-flips-to-make-a-or-b-equal-to-c
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        list_a = []
        list_b = []
        list_c = []
        count = 0
        while a > 0:
            list_a.append(a % 2)
            a = int(a / 2)
        while b > 0:
            list_b.append(b % 2)
            b = int(b / 2)
        while c > 0:
            list_c.append(c % 2)
            c = int(c / 2)
        max_length = max(len(list_a), len(list_b), len(list_c))
        while len(list_a) < max_length:
            list_a.append(0)
        while len(list_b) < max_length:
            list_b.append(0)
        while len(list_c) < max_length:
            list_c.append(0)
        for i in range(len(list_c)):
            if list_c[i] == 0:
                if list_a[i] == 1:
                    count += 1
                if list_b[i] == 1:
                    count += 1
            #         wei 1
            else:
                if list_a[i] == 0 and list_b[i] == 0:
                    count += 1
        return count

demo = Solution()
print(demo.minFlips(8,3,5))
print(demo.minFlips(2,6,5))