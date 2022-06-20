
"""
感觉像是动态规划问题
最后一个棋子，他的距离是以下两种情况：
1，由前一个棋子的操作次数+1
2，由具有相同值的元素，最小步数+1
当最后一个棋子确定后，还需要对他之前的棋子做一个校正

如果之前的棋子的步数改变了，那么有他进行下一步跳跃的棋子也要改变呀

相同的元素，其步数肯定是第一个元素加一
"""
import sys
from collections import defaultdict
from typing import List

# class Solution:
#     def minJumps(self, arr: List[int]) -> int:
#         d = {}
#         # d2 = defaultdict(list)
#         d2 = {}
#         for k in set(arr):
#             d[k] = sys.maxsize
#             d2[k] = arr.index(k)
#         # for k in range(len(arr)):
#         #     d2[arr[k]].append(k)
#         d[arr[0]] = 1
#         steps = [sys.maxsize]*len(arr)
#         steps[0] = 0
#         for i in range(1, len(arr)):
#             # 右边的数
#             a = min(d[arr[i + 1]],steps[i+1]) + 1 if i + 1 < len(arr) else sys.maxsize
#             # 左边的数
#             b = min(d[arr[i - 1]],steps[i-1]) + 1 if i - 1 >= 0 else sys.maxsize
#             # 上一个相同的数
#             c = d[arr[i]]
#             step = min(a, b, c)
#             steps[i] = step
#             d[arr[i]] = step+1 if d[arr[i]] > step+1 else d[arr[i]]
#             k = i - 1
#             while k > 0:
#                 if d[arr[k]] > step + 1:
#                     if d2[arr[k]] != k:
#                         d[arr[k]] = step + 1
#                     k -= 1
#                     step += 1
#                 else:
#                     break
#
# # step = min(steps[i+1]+1 if i + 1 < len(arr) else sys.maxsize,steps[i-1]+1 if i-1>=0 else sys.maxsize,steps[i]) #
# steps[i] = step # for k in d2[arr[i]]: #     if k > i: #         steps[k] = step + 1 if step+1 < steps[k] else
# steps[k] return steps[-1]
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = {}
        # d2 = defaultdict(list)
        d2 = defaultdict(list)
        d3 = {}
        steps = [-1] * len(arr)

        for k in set(arr):
            d[k] = False
            d3[k] = -1
        for i in range(len(arr)):
            d2[arr[i]].append(i)
        step = 0
        d[arr[0]] = True
        d3[arr[0]] = step
        next_level = [0]
        while True:
            temp = []
            for i in next_level:
                for j in d2[arr[i]]:
                    if j - 1 > 0:
                        if d[arr[j-1]] is False:
                            d[arr[j-1]] = True
                            temp.append(j-1)
                    if j + 1 < len(arr):
                        if d[arr[j+1]] is False:
                            d[arr[j+1]] = True
                            temp.append(j+1)
                d3[arr[i]] = step
            next_level = set(temp)
            if d[arr[-1]] is True and d3[arr[-1]] != -1:
                return d3[arr[-1]] if len(arr)-1 == d2[arr[-1]][-1] else d3[arr[-1]]+1
            step += 1



# demo = Solution()
# print(demo.minJumps([-76,3,66,-32,64,2,-19,-8,-5,-93,80,-5,-76,-78,64,2,16]))
# print(demo.minJumps([6,1,9]))
# print(demo.minJumps(arr = [100,-23,-23,404,100,23,23,23,3,404]))


demo = Solution()
# print(demo.minJumps([68,-94,-44,-18,-1,18,-87,29,-6,-87,-27,37,-57,7,18,68,-59,29,7,53,-27,-59,18,-1,18,-18,-59,-1,-18,-84,-20,7,7,-87,-18,-84,-20,-27]))
print(demo.minJumps([25,-28,-51,61,-74,-51,-30,58,36,68,-80,-64,25,-30,-53,36,-74,61,-100,-30,-52]))
# print(demo.minJumps([7,7,2,1,7,7,7,3,4,1]))
# print(demo.minJumps([-76, 3, 66, -32, 64, 2, -19, -8, -5, -93, 80, -5, -76, -78, 64, 2, 16]))
# print(demo.minJumps([6, 1, 9]))
print(demo.minJumps(arr=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
