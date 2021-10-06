# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        def middle_sear(node: TreeNode) -> []:
            """
            使用动态规划加后序遍历树
            :param node:
            :return:
            """
            left = right = []
            if node.left is None and node.right is None:
                return [node.val, 0, True]
            if node.left:
                left = middle_sear(node.left)
            if node.right:
                right = middle_sear(node.right)
            if len(left) > 0 and len(right) > 0:
                if not left[-1] and not right[-1]:
                    return [left[0] + right[0] + node.val, left[0] + right[0], True]
                elif not left[-1] and right[-1]:
                    if node.val + left[0] + right[1] >= left[0] + right[0]:
                        return [left[0] + right[1] + node.val, left[0] + right[0], True]
                elif left[-1] and not right[-1]:
                    if left[1] + right[0] + node.val >= left[0] + right[0]:
                        return [left[1] + right[0] + node.val, left[0] + right[0], True]
                elif left[-1] and right[-1]:
                    if node.val + left[1] + right[1] >= left[0] + right[0]:
                        return [left[1] + right[1] + node.val, left[0] + right[0], True]
                return [left[0] + right[0], left[0] + right[0], False]
            if len(left) > 0:
                if not left[-1]:
                    return [left[1] + node.val, left[1], True]
                else:
                    if node.val+left[1] >= left[0]:
                        return [left[1] + node.val, left[0], True]
                    else:
                        return [left[0], left[0], False]
            if len(right) > 0:
                if not right[-1]:
                    return [right[1] + node.val, right[1], True]
                else:
                    if node.val+right[1] >= right[0]:
                        return [right[1] + node.val, right[0], True]
                    else:
                        return [right[0], right[0], False]

        a = middle_sear(root)
        return a[0]
