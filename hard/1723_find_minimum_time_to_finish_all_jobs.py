# 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
#
# 请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，
# 且每项工作只能分配给一位工人。
# 工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。
# 请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
#
# 返回分配方案中尽可能 最小 的 最大工作时间 。
import copy
import math
import sys
from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:

        def check(limit):
            # 剪枝：排序后，大的先拿出来试，如果方案不行，失败得更快
            arr = sorted(jobs)

            groups = [0] * k
            # 分成K 组，看看在这个limit 下 能不能安排完工作
            if backtrace(arr, groups, limit):
                return True
            else:
                return False

        def backtrace(arr, groups, limit):
            # 尝试每种可能性
            # print(arr, groups, limit)
            if not arr: return True  # 分完，则方案可行
            v = arr.pop()

            for i in range(len(groups)):
                if groups[i] + v <= limit:
                    groups[i] += v
                    if backtrace(arr, groups, limit):
                        return True
                    groups[i] -= v

                    # 如果这个工人分活失败（给他分配这个任务后所有的尝试都是失败的），则剪枝，因为也没必要再往后试了，其他人也会出现一样的情况
                    if groups[i] == 0:
                        break

            arr.append(v)

            return False

        # 每个人承担的工作的上限，最小为，job 里面的最大值，最大为 jobs 之和
        l, r = max(jobs), sum(jobs)

        while l < r:
            mid = (l + r) // 2

            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l





demo = Solution()
print(demo.minimumTimeRequired(
    [9899456, 8291115, 9477657, 9288480, 5146275, 7697968, 8573153, 3582365, 3758448, 9881935, 2420271, 4542202]
    , 9))
print(demo.minimumTimeRequired(
    [5, 5, 4, 4, 4]
    , 2))
print(demo.minimumTimeRequired(jobs=[3, 2, 3], k=3))
print(demo.minimumTimeRequired(jobs=[1, 2, 4, 7, 8], k=2))
