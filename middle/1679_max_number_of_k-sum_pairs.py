# 给你一个整数数组 nums 和一个整数 k 。
#
# 每一步操作中，你需要从数组中选出和为 k 的两个整数，并将它们移出数组。
#
# 返回你可以对数组执行的最大操作数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/max-number-of-k-sum-pairs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        count = 0
        for i in nums:
            d[i] += 1
        for i in sorted(d.keys()):

            if d[i] > 0 and d[k - i] > 0:
                if i == k/2:
                    c = int(d[i]/2)
                    count += c
                    d[i] -= c*2
                else:
                    c = min(d[i], d[k - i])
                    count += c
                    d[i] -= c
                    d[k - i] -= c
        return count
