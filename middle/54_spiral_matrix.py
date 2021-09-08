from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        result = [matrix[0][0]]
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        prev = [0,1]
        position = [0,0]
        d = [[False for _ in range(n)] for _ in range(m)]
        d[0][0] = True
        tag = True
        while tag:
            if position[0]+prev[0]<m and position[1]+prev[1] < n and not d[position[0]+prev[0]][position[1]+prev[1]]:
                position[0] = position[0]+prev[0]
                position[1] = position[1]+prev[1]
                result.append(matrix[position[0]][position[1]])
                d[position[0]][position[1]] = True
            else:
                o = False
                for direc in direction:
                    if position[0] + direc[0] < m and position[1] + direc[1] < n and \
                            not d[position[0]+direc[0]][position[1]+direc[1]]:
                        o = True
                        prev = [direc[0],direc[1]]
                        position[0] = position[0] + direc[0]
                        position[1] = position[1] + direc[1]
                        result.append(matrix[position[0]][position[1]])
                        d[position[0]][position[1]] = True
                        break
                if not o:
                    tag = False
        return result


demo = Solution()
print(demo.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(demo.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))








