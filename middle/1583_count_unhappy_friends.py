# 给你一份 n 位朋友的亲近程度列表，其中 n 总是 偶数 。
#
# 对每位朋友 i，preferences[i] 包含一份按亲近程度从高到低排列
# 的朋友列表。换句话说，排在列表前面的朋友与 i 的亲近程度比排在列表后面的朋友更高。
# 每个列表中的朋友均以 0 到 n-1 之间的整数表示。
#
# 所有的朋友被分成几对，配对情况以列表 pairs 给出，
# 其中 pairs[i] = [xi, yi] 表示 xi 与 yi 配对，且 yi 与 xi 配对。
#
# 但是，这样的配对情况可能会是其中部分朋友感到不开心。
# 在 x 与 y 配对且 u 与 v 配对的情况下，
# 如果同时满足下述两个条件，x 就会不开心：
#
# x 与 u 的亲近程度胜过 x 与 y，且
# u 与 x 的亲近程度胜过 u 与 v
# 返回 不开心的朋友的数目 。
from collections import defaultdict
from typing import List

# 二位哈希数组可以不用整的
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        d = [defaultdict(int) for _ in range(n)]
        d_pairs = defaultdict()
        count = 0
        tag = False
        # 做个二维哈希表记录亲密度
        for i in range(n):
            max = n - 1
            for j in range(n - 1):
                d[i][preferences[i][j]] = max
                max -= 1
        for i in range(len(pairs)):
            d_pairs[pairs[i][0]] = pairs[i][1]
            d_pairs[pairs[i][1]] = pairs[i][0]
        for i in range(len(pairs)):
            for j in range(0, 2):
                x = pairs[i][j]
                y = pairs[i][(j + 1) % 2]
                for k, value in d[x].items() :
                    if k == y:
                        break
                    else:
                        u = k
                        v = d_pairs[u]
                        for u_k in d[u].keys():
                            if u_k == v:
                                tag = False
                                break
                            if u_k == x:
                                tag = True
                                break
                    if tag:
                        count += 1
                        break
                tag = False
        return count

demo = Solution()
print(demo.unhappyFriends(4
                    , [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
                    , [[0, 1], [2, 3]]))
print(demo.unhappyFriends(n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]))
