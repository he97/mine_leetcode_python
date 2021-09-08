# 第i个人的体重为people[i]，每艘船可以承载的最大重量为limit。
#
# 每艘船最多可同时载两人，但条件是这些人的重量之和最多为limit。
#
# 返回载到每一个人所需的最小船数。(保证每个人都能被船载)。
#
#
#
# 来源：力扣（LeetCode）
# 链接：https: // leetcode - cn.com / problems / boats - to - save - people
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import math
from collections import defaultdict
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        d = defaultdict(int)
        boat = 0
        for i in people:
            d[i] += 1
        n = max(d.keys())
        boat += d[limit]
        d[limit] = 0
        index = int(limit / 2)
        while index <= n:
            if d[index] > 0:
                if d[limit - index] > 0:
                    data = min(d[index], d[limit - index])
                    d[index] -= data
                    d[limit - index] -= data
                    boat += data
            index += 1
        index = int(limit / 2) + 1
        k = int(limit / 2)
        j = k
        while index <= n:
            if d[index] > 0:
                while d[index] > 0:
                    while j > 0:
                        if d[j] > 0 and index + j <= limit:
                            break
                        else:
                            j -= 1
                    if j != 0 and index + j <= limit:
                        data = min(d[index], d[j])
                        d[index] -= data
                        d[j] -= data
                        boat += data
                    else:
                        boat += d[index]
                        d[index] = 0
            if d[index] == 0:
                index += 1

        left = 0
        right = 0
        for i in d.keys():
            if i <= math.floor(limit / 2):
                left += d[i]
            else:
                right += d[i]
        boat += math.ceil(left / 2)
        boat += math.ceil(right / 2)
        return boat


demo = Solution()
print(demo.numRescueBoats([44, 10, 29, 12, 49, 41, 23, 5, 17, 26]
                          , 50))
print(demo.numRescueBoats([5, 1, 4, 2], 6))
print(demo.numRescueBoats([9, 4, 6], 9))
print(demo.numRescueBoats([2, 4], 5))
print(demo.numRescueBoats(people=[1, 2], limit=3))
print(demo.numRescueBoats(people=[3, 2, 2, 1], limit=3))
print(demo.numRescueBoats(people=[3, 5, 3, 4], limit=5))
