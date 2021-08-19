# You are given a string s consisting only of characters 'a' and 'b'​​​​.
#
# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
#
# Return the minimum number of deletions needed to make s balanced.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-deletions-to-make-string-balanced
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List

# 以下方法时间消耗过高
# 学习动态规划再来吧
class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_list_indexes = []
        b_list_indexes = []
        index = 0
        for index in range(0, len(s)):
            if s[index] == 'b':
                break
        while index < len(s):
            if s[index] == 'b':
                b_list_indexes.append(index)
            else:
                a_list_indexes.append(index)
            index += 1
        if 0 == len(a_list_indexes) or len(b_list_indexes) == 0:
            return 0

        max_delete = len(a_list_indexes) if len(a_list_indexes) < len(b_list_indexes) else len(b_list_indexes)
        # 逆转一下数组，反着的计算有些折磨
        a_list_indexes.reverse()
        # i:会删除多少个数字
        for i in range(1, max_delete):
            if self.delete_num_and_check(a_list_indexes=a_list_indexes,
                                         b_list_indexes=b_list_indexes,
                                         delete_num=i):
                return i
        return max_delete

    #     如果对某个数目
    def delete_num_and_check(self,
                             delete_num: int,
                             a_list_indexes: List[int],
                             b_list_indexes: List[int]) -> bool:
        for i in range(0, delete_num):
            # 判断a的最大的索引与b的最小的索引的位置
            if a_list_indexes[i] < b_list_indexes[delete_num - i]:
                # a_list_indexes.reverse()
                return True
        return False


demo = Solution()
result = demo.minimumDeletions(s="aaaaaabbbbabaaaabbabaaabbabbbaaabababaaaaaaabbaaabaaababaaabababa")
print(result)
