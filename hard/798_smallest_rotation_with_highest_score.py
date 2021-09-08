# 给定一个数组A，我们可以将它按一个非负整数 K进行轮调，这样可以使数组变为A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1]的形式。此后，任何值小于或等于其索引的项都可以记作一分。
# 
# 例如，如果数组为[2, 4, 1, 3, 0]，我们按K = 2进行轮调后，它将变成[1, 3, 0, 2, 4]。这将记作 3 分，因为 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point]。
# 
# 在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调索引 K。如果有多个答案，返回满足条件的最小的索引 K。
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/smallest-rotation-with-highest-score
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        # d = [[0 for _ in range(n)] for i in range(n)]
        score = [0 for _ in range(n)]
        k = 0

        def add(start, end):
            for index in range(start, end):
                score[index] += 1

        while k < n:
            if k < nums[k]:
                score[k + 1] += 1
                if n - nums[k] + k + 1 < n:
                    score[n - nums[k] + k + 1] -= 1
                # add(k + 1, n - nums[k] + k + 1)
            # elif k == nums[k]:
            #     score[0] += 1
            #     score[1] -= 1
            #     score[nums[k]+1] += 1
            #     score[n-1] -= 1
            #     # add(nums[k]+1, n)
            elif k >= nums[k]:
                score[0] += 1
                if k - nums[k] + 1 < n:
                    score[k - nums[k] + 1] -= 1
                    if k + 1 < n:
                        score[k + 1] += 1
                # score[n-1] -= 1
                # add(0, k - nums[k]+1)_
                # add(k + 1, n)
            k += 1
        best = -len(nums)
        ans = cur = 0
        for i, score in enumerate(score):
            cur += score
            if cur > best:
                best = cur
                ans = i
        # max_score = max(score)
        return ans


# class Solution(object):
#     def bestRotation(self, A):
#         N = len(A)
#         bad = [0] * N
#         for i, x in enumerate(A):
#             left, right = (i - x + 1) % N, (i + 1) % N
#             bad[left] -= 1
#             bad[right] += 1
#             if left > right:
#                 bad[0] -= 1
#
#         best = -N
#         ans = cur = 0
#         for i, score in enumerate(bad):
#             cur += score
#             if cur > best:
#                 best = cur
#                 ans = i
#
#         return ans


demo = Solution()
print(demo.bestRotation([6,2,8,3,5,2,4,3,7,6]))
print(demo.bestRotation([2, 3, 1, 4, 0]))
print(demo.bestRotation([1, 3, 0, 2, 4]))
