# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
class Solution:
    def reverseVowels(self, s: str) -> str:
        list_s = list(s)
        i = 0
        j = len(list_s) - 1
        d = ['a','e','i','o','u','A','E','I','O','U']
        while i < j:
            if list_s[i] in d and list_s[j] not in d:
                j -= 1
            elif list_s[i] not in d and list_s[j] in d:
                i += 1
            elif list_s[i] in d and list_s[j] in d:
                temp = list_s[i]
                list_s[i] = list_s[j]
                list_s[j] = temp
                i += 1
                j -= 1
            elif list_s[i] not in d and list_s[j] not in d:
                j -= 1
                i += 1
        return ''.join(list_s)


demo = Solution()
print(demo.reverseVowels('leetcode'))
