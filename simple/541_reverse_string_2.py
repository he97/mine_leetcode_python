# 给定一个字符串 s 和一个整数 k，从字符串开头算起，
# 每 2k 个字符反转前 k 个字符。
#
# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，
# 则反转前 k 个字符，其余字符保持原样。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-string-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list_s = list(s)
        i = 0
        for i in range(0, len(list_s), 2 * k):
            if i + k - 1 >= len(list_s):
                end_index = len(list_s) - 1
            else:
                end_index = i + k - 1
            index = i
            while index < end_index:
                temp = list_s[index]
                list_s[index] = list_s[end_index]
                list_s[end_index] = temp
                index += 1
                end_index -= 1
        # if i + k - 1 > len(list_s):
        #     end_index = len(list_s) - 1
        # else:
        #     end_index = i + k - 1
        # index = i
        # while index < end_index:
        #     temp = list_s[index]
        #     list_s[index] = list_s[end_index]
        #     list_s[end_index] = temp
        #     index += 1
        #     end_index -= 1
        return ''.join(list_s)


demo = Solution()
print(demo.reverseStr('abcdefg',k=2))
print(demo.reverseStr('abcd',k=2))
