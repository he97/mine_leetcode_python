# 峰值元素是指其值严格大于左右相邻值的元素。
# 
# 给你一个整数数组nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
# 
# 你可以假设nums[-1] = nums[n] = -∞ 。
# 
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-peak-element
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import random
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        def get(index: int):
            if index < 0 or index >= n:
                return float('-inf')
            else:
                return nums[index]

        left, right, ans= 0,n-1, n-1
        while left< right:
            a = (left + right) // 2
            if get(a-1) < get(a) > get(a+1):
                ans = a
                break
            elif get(a) > get(a-1):
                left = a + 1
                ans = n-1
            else:
                right = a - 1
                ans = 0
        return ans