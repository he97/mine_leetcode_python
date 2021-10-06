# 请你判断一个9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
#
# 数字1-9在每一行只能出现一次。
# 数字1-9在每一列只能出现一次。
# 数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）
# 数独部分空格内已填入了数字，空白格用'.'表示。
#
# 注意：
#
# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-sudoku
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        square = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    a = int(board[i][j]) - 1
                    if not row[i][a]:
                        row[i][a] = True
                    else:
                        return False
                    if not column[j][a]:
                        column[j][a] = True
                    else:
                        return False
                    if not square[i // 3][j // 3][a]:
                        square[i // 3][j // 3][a] = True
                    else:
                        return False
        return True
