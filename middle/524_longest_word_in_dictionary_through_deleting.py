from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        string = list(s)
        word = ''
        length = 0
        for i in dictionary:
            a = list(i)
            j = 0
            k = 0
            while j < len(a) and k < len(string):
                if a[j] == string[k]:
                    j += 1
                    k += 1
                else:
                    k += 1
            if j == len(a):
                if len(a) > length:
                    length = len(a)
                    word = i
                elif len(a) == length:
                    if word != '':
                        word = min(word, i)
                    else:
                        word = i
        return word


demo = Solution()
print(demo.findLongestWord("abce"
,["abe","abc"]))