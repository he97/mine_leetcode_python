# 有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。
#
# 现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/1-bit-and-2-bit-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        tag = 0
        pre = 1
        for i in range(0, len(bits)):
            if bits[i] == 1:
                if pre == 2 and tag == 1:
                    tag = 0
                elif pre == 1 and tag == 0:
                    pre = 2
                    tag = 1
                elif pre == 2 and tag == 0:
                    pre = 2
                    tag = 1
            #         case 0
            else:
                if pre == 2 and tag == 1:
                    pre = 2
                    tag = 0
                elif pre == 2 and tag == 0:
                    pre = 1
                else:
                    tag = 0
                    pre = 1
        if pre == 1:
            return True
        else:
            return False

demo = Solution()
print(demo.isOneBitCharacter([1,1,1,0]))

print(demo.isOneBitCharacter([1,0,0]))
print(demo.isOneBitCharacter([1,1,0]))
