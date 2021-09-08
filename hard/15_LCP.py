import sys
from typing import List


class Solution:
    def visitOrder(self, points: List[List[int]], direction: str) -> List[int]:
        direc = list(direction)
        result = []
        used = [False for _ in range(len(points))]

        def get_k(point_a: list, point_b: list):
            if point_a[1] - point_b[1] == 0:
                return sys.maxsize
            elif point_a[0] - point_b[0] == 0:
                return 0
            else:
                return (point_a[0] - point_b[0]) / (point_a[1] - point_b[1])
        def get_k_2(point_a: list, point_b: list):
            if point_a[1] - point_b[1] == 0:
                return 0
            elif point_a[0] - point_b[0] == 0:
                return -sys.maxsize
            else:
                return (point_a[0] - point_b[0]) / (point_a[1] - point_b[1])
        index = 0
        left = 10001
        for i in range(len(points)):
            if left > points[i][0]:
                left = points[i][0]
                index = i
        prev = [points[index][0], points[index][1]]
        result.append(index)
        used[index] = True
        for j in range(len(direc)):
            if direc[j] == 'L':
                ratio = sys.maxsize
                index = 0
                for i in range(len(points)):
                    if not used[i]:
                        a = get_k(prev, points[i])
                        if ratio > a:
                            ratio = a
                            index = i
                prev = [points[index][0], points[index][1]]
                result.append(index)
                used[index] = True
            elif direc[j] == 'R':
                ratio = -sys.maxsize
                index = 0
                for i in range(len(points)):
                    if not used[i]:
                        a = get_k_2(prev, points[i])
                        if ratio < a:
                            ratio = a
                            index = i
                prev = [points[index][0], points[index][1]]
                result.append(index)
                used[index] = True
        for i in range(len(used)):
            if not used[i]:
                result.append(i)
                break
        return result

demo = Solution()
print(demo.visitOrder([[1,1],[1,4],[3,2],[2,1]]
,"LL"))
print(demo.visitOrder([[1,3],[2,4],[3,3],[2,1]]
,"LR"))