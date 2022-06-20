# 你正在参加一个多角色游戏，每个角色都有两个主要属性：攻击 和 防御 。给你一个二维整数数组 properties ，其中 properties[i] = [attacki, defensei] 表示游戏中第 i 个角色的属性。
#
# 如果存在一个其他角色的攻击和防御等级 都严格高于 该角色的攻击和防御等级，则认为该角色为 弱角色 。更正式地，如果认为角色 i 弱于 存在的另一个角色 j ，那么 attackj > attacki 且 defensej > defensei 。
#
# 返回 弱角色 的数量。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/the-number-of-weak-characters-in-the-game
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import heapq
from collections import defaultdict
from typing import List

"""
每个元素两个值，i，j
defaultdict 然后
"""


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        d = defaultdict(list)
        for i in properties:
            d[i[0]].append(i[1])
        ans = 0
        a = max(d[max(d.keys())])
        # print(d)
        for i in sorted(d.keys(), reverse=True)[1:]:
            # print(max(d[i]))
            heapq.heapify(d[i])
            x = max(d[i])
            while True:
                if len(d[i]) > 0:
                    z = heapq.heappop(d[i])
                    if z < a:
                        ans += 1
                        continue
                    else:
                        break
                else:
                    break
            a = max(a, x)
        return ans



