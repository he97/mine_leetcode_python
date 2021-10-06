from typing import List


# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
#
# 单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        d = {}
        result = []
        for i in words:
            if i[0] not in d.keys():
                d[i[0]] = [list(i)]
            else:
                d[i[0]].append(list(i))
        direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visit = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                l = list(board[i][j])
                if l[0] in d.keys():
                    p = []
                    for z in d[l[0]]:
                        visit[i][j] = True
                        a = [[i, j]]
                        index = 1
                        while len(a) > 0 and index < len(z):
                            temp = []
                            for x in a:
                                tag = False
                                for direc in direction:
                                    c = direc[0] + x[0]
                                    f = direc[1] + x[1]
                                    if 0 <= c < m and 0 <= f < n and not visit[c][f] and board[c][f] == z[index]:
                                        tag = True
                                        visit[c][f] = True
                                        temp.append([c, f])
                                if not tag:
                                    visit[x[0]][x[1]] = False

                            a = temp
                            index += 1
                        if len(a) > 0:
                            result.append(''.join(z))
                            p.append(z)
                        visit = [[False] * n for _ in range(m)]
                    for _ in p:
                        d[l[0]].remove(_)
        return result


demo = Solution()
print(demo.findWords([["a", "b", "c"], ["a", "e", "d"], ["a", "f", "g"]]
                     , ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"]))
print(demo.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
                     , ["oath", "pea", "eat", "rain", "hklf", "hf"]))
print(demo.findWords([["o"
                          , "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]]
                     , ["oa", "oaa"]))
print(demo.findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                     words=["oath", "pea", "eat", "rain"]))
