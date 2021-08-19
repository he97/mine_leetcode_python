# from typing import List
#
#
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         d = []
#         for n in nums:
#             if not d or n > d[-1]:
#                 d.append(n)
#             else:
#                 l, r = 0, len(d) - 1
#                 loc = r
#                 while l <= r:
#                     mid = (l + r) // 2
#                     if d[mid] >= n:
#                         loc = mid
#                         r = mid - 1
#                     else:
#                         l = mid + 1
#                 d[loc] = n
#         return len(d)
# demo = Solution()
# result = demo.lengthOfLIS([0,8,4,12,2,3])
# print(result)
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-by-leetcode-soluti/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
for i in range(10, -4):
    print(i)