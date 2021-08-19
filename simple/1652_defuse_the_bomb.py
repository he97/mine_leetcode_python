# You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.
#
# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
#
# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
#
# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/defuse-the-bomb
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 拆炸弹问题
from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        replace_number = 0
        new_code = []
        if k >= 0:
            symbol = 1
        else:
            symbol = -1
        for i in range(0, len(code)):
            for code_index in range(1, abs(k)+1):
                replace_number += code[((i + symbol*code_index + len(code)) % len(code))]
            new_code.append(replace_number)
            replace_number = 0
        return new_code


demo = Solution()
demo.decrypt(code=[2, 4, 9, 3],
             k=-2)
# demo.decrypt(code=[5, 7, 1, 4],
#              k=3)
