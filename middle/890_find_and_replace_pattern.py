# 你有一个单词列表words和一个模式pattern，你想知道 words 中的哪些单词与模式匹配。
# 
# 如果存在字母的排列 p，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。
# 
# （回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）
# 
# 返回 words 中与给定模式匹配的单词列表。
# 
# 你可以按任何顺序返回答案。
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-and-replace-pattern
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        p = list(pattern)
        d = {p[0]: 1}
        data = 1
        count = 2
        w = []
        o = []
        for i in range(1, len(p)):
            if p[i] not in d.keys():
                d[p[i]] = count
                count += 1
            data = data * 10 + d[p[i]]
        for i in range(len(words)):
            c = list(words[i])
            d = {c[0]: 1}
            data_words = 1
            z = 2
            for k in range(1, len(c)):
                if c[k] not in d.keys():
                    d[c[k]] = z
                    z += 1
                data_words = data_words * 10 + d[c[k]]
            w.append(data_words)
        for i in range(len(w)):
            if w[i] == data:
                o.append(words[i])
        return o

demo = Solution()
print(demo.findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))