# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # 使用数组暂存 还是使用层次搜索 但是最后要加上本次的节点值
        if root == None:
            return 0
        a = [[root.val, root]]
        count = 0
        if root.val == targetSum:
            count += 1
        while len(a) > 0:
            temp = []
            for i in a:
                temp_t = []
                if i[-1].right is not None:
                    for j in range(len(i) - 1):
                        if i[j] + i[-1].right.val == targetSum:
                            count += 1
                        temp_t.append(i[j] + i[-1].right.val)
                    if i[-1].right.val == targetSum:
                        count += 1
                    temp_t.append(i[-1].right.val)
                    temp_t.append(i[-1].right)
                    temp.append(temp_t)
                    temp_t = []
                if i[-1].left is not None:
                    for j in range(len(i) - 1):
                        if i[j] + i[-1].left.val == targetSum:
                            count += 1
                        temp_t.append(i[j] + i[-1].left.val)
                    if i[-1].left.val == targetSum:
                        count += 1
                    temp_t.append(i[-1].left.val)
                    temp_t.append(i[-1].left)
                    temp.append(temp_t)
            a = temp
        return count
