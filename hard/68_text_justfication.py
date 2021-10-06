#
# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
#
# 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。
#
# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
#
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。
#
# 说明:
#
# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        d = []
        n = len(words)
        result = []
        for i in range(n):
            d.append(list(words[i]))
        i = 0
        while i < n:
            s = ''
            temp = []
            length = 0
            chr_length = 0
            # 统计字符的时候 应该考虑到每个字符应该有最少的一个空格
            #
            while i < n and length + len(d[i]) <= maxWidth:
                temp.append(d[i])
                length += len(d[i]) + 1
                i += 1
            #     最后一行
            if i >= n:
                m = len(temp)
                spaces = maxWidth - length + m
                for k in temp:
                    s += ''.join(k)
                    if spaces > 0:
                        s += ' '
                        spaces -= 1
                for j in range(spaces):
                    s += ' '
                result.append(s)
            #     不是最后一行
            else:
                m = len(temp)
                spaces = maxWidth - length + m
                if m == 1:
                    s += ''.join(temp[0])
                    for x in range(spaces):
                        s += ' '
                else:
                    a = int(spaces / (m - 1))
                    b = spaces % (m - 1)
                    for k in range(b):
                        s += ''.join(temp[k])
                        for x in range(a + 1):
                            s += ' '
                    for k in range(b, m - 1):
                        s += ''.join(temp[k])
                        for x in range(a):
                            s += ' '
                    s += ''.join(temp[m - 1])
                result.append(s)
        return result
