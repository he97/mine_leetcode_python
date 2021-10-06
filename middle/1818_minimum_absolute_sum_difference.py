# 给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。
#
# 数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 <= i < n）的 总和（下标从 0 开始）。
#
# 你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。
#
# 在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 109 + 7 取余 后返回。
#
# |x| 定义为：
#
# 如果 x >= 0 ，值为 x ，或者
# 如果 x <= 0 ，值为 -x
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-absolute-sum-difference
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import sys
from typing import List


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        c = set(nums1)
        a = [-sys.maxsize] + sorted(set(c)) + [sys.maxsize]
        replace_gap = 0
        count = 0
        for i in range(len(nums1)):
            gap = abs(nums1[i] - nums2[i])
            count += gap
            j = 1
            k = len(a)-1
            mid = (j + k) // 2
            while j < k:
                mid = (j + k) // 2
                if a[mid] == nums2[i]:
                    if gap > replace_gap:
                        replace_gap = gap
                    break
                elif a[mid + 1] > nums2[i] > a[mid]:
                    if abs(a[mid + 1] - nums2[i]) < gap and gap - abs(a[mid + 1] - nums2[i]) > replace_gap:
                        replace_gap = gap - abs(a[mid + 1] - nums2[i])
                    if abs(a[mid] - nums2[i]) < gap and gap - abs(a[mid] - nums2[i]) > replace_gap:
                        replace_gap = gap - abs(a[mid] - nums2[i])
                    break
                elif a[mid] > nums2[i] > a[mid - 1]:
                    if abs(a[mid] - nums2[i]) < gap and gap - abs(a[mid] - nums2[i]) > replace_gap:
                        replace_gap = gap - abs(a[mid] - nums2[i])
                    if abs(a[mid - 1] - nums2[i]) < gap and gap - abs(a[mid - 1] - nums2[i]) > replace_gap:
                        replace_gap = gap - abs(a[mid - 1] - nums2[i])
                    break
                elif a[mid] > nums2[i]:
                    k = mid - 1
                elif a[mid] < nums2[i]:
                    j = mid + 1
            # print('a[mid]:{0},nums2[i]:'.format(a[mid], nums2[i]))
            if mid + 1 < len(a):
                if abs(a[mid + 1] - nums2[i]) < gap and gap - abs(a[mid + 1] - nums2[i]) > replace_gap:
                    replace_gap = gap - abs(a[mid + 1] - nums2[i])
            if mid - 1 > 0:
                if abs(a[mid - 1] - nums2[i]) < gap and gap - abs(a[mid - 1] - nums2[i]) > replace_gap:
                    replace_gap = gap - abs(a[mid - 1] - nums2[i])
        return (count - replace_gap) % (10**9+7)

demo = Solution()
print(demo.minAbsoluteSumDiff([1,7,5]
,[2,3,5]))
print(demo.minAbsoluteSumDiff([57,42,21,28,30,25,22,12,55,3,47,18,43,29,20,44,59,9,43,7,8,5,42,53,99,34,37,88,87,62,38,68,31,3,11,61,93,34,63,27,20,48,38,5,71,100,88,54,52,15,98,59,74,26,81,38,11,44,25,69,79,81,51,85,59,84,83,99,31,47,31,23,83,70,82,79,86,31,50,17,11,100,55,15,98,11,90,16,46,89,34,33,57,53,82,34,25,70,5,1]
,[76,3,5,29,18,53,55,79,30,33,87,3,56,93,40,80,9,91,71,38,35,78,32,58,77,41,63,5,21,67,21,84,52,80,65,38,62,99,80,13,59,94,21,61,43,82,29,97,31,24,95,52,90,92,37,26,65,89,90,32,27,3,42,47,93,25,14,5,39,85,89,7,74,38,12,46,40,25,51,2,19,8,21,62,58,29,32,77,62,9,74,98,10,55,25,62,48,48,24,21]))