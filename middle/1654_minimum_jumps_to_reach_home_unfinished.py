# 有一只跳蚤的家在数轴上的位置x处。请你帮助它从位置0出发，到达它的家。
#
# 跳蚤跳跃的规则如下：
#
# 它可以 往前 跳恰好 a个位置（即往右跳）。
# 它可以 往后跳恰好 b个位置（即往左跳）。
# 它不能 连续 往后跳 2 次。
# 它不能跳到任何forbidden数组中的位置。
# 跳蚤可以往前跳 超过它的家的位置，但是它 不能跳到负整数的位置。
#
# 给你一个整数数组forbidden，其中forbidden[i]是跳蚤不能跳到的位置，同时给你整数a，b和x，请你返回跳蚤到家的最少跳跃次数。如果没有恰好到达 x的可行方案，请你返回 -1 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-jumps-to-reach-home
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        return 0