# 如果一棵二叉树满足下述几个条件，则可以称为 奇偶树 ：
#
# 二叉树根节点所在层下标为 0 ，根的子节点所在层下标为 1 ，根的孙节点所在层下标为 2 ，依此类推。
# 偶数下标 层上的所有节点的值都是 奇 整数，从左到右按顺序 严格递增
# 奇数下标 层上的所有节点的值都是 偶 整数，从左到右按顺序 严格递减
# 给你二叉树的根节点，如果二叉树为 奇偶树 ，则返回 true ，否则返回 false 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/even-odd-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.
import sys
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root.val % 2 != 1:
            return False
        level = [root]
        level_temp = []
        is_odd = 1
        while len(level) > 0:
            # print(level)
            # print('level over this level: node count:{0}'.format(len(level)))
            prev = sys.maxsize if is_odd == 1 else -sys.maxsize
            for k in range(len(level)):
                if is_odd == 1:
                    if level[k].left is not None:
                        if level[k].left.val < prev and level[k].left.val % 2 == 0:
                            prev = level[k].left.val
                            level_temp.append(level[k].left)
                        else:
                            return False
                    if level[k].right is not None:
                        if level[k].right.val < prev and level[k].right.val % 2 == 0:
                            prev = level[k].right.val
                            level_temp.append(level[k].right)
                        else:
                            return False
                else:
                    if level[k].left is not None:
                        if level[k].left.val > prev and level[k].left.val % 2 != 0:
                            prev = level[k].left.val
                            level_temp.append(level[k].left)
                        else:
                            return False
                    if level[k].right is not None:
                        if level[k].right.val > prev and level[k].right.val % 2 != 0:
                            prev = level[k].right.val
                            level_temp.append(level[k].right)
                        else:
                            return False
            is_odd = not is_odd
            level = level_temp if len(level_temp) > 0 else []
            level_temp = []
        return True
