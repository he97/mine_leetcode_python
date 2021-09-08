# 给你一个由不同字符组成的字符串allowed和一个字符串数组words。
# 如果一个字符串的每一个字符都在 allowed中，就称这个字符串是 一致字符串 。
#
# 请你返回words数组中一致字符串 的数目。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-the-number-of-consistent-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        p = list(allowed)
        d = [False for _ in range(26)]
        count = 0
        for i in range(len(p)):
            if not d[ord(p[i])-97]:
                d[ord(p[i]) - 97] = True
        for i in words:
            p = list(i)
            tag = True
            for k in range(len(p)):
                if not d[ord(p[k]) - 97]:
                    tag = False
                    break
            if tag:
                count += 1
        return count


demo = Solution()
print(demo.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))
