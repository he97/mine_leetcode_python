# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        data = []
        def get_info(node:TreeNode):
            if node.left is not None:
                get_info(node.left)
            data.append(node.val)
            if node.right is not None:
                get_info(node.right)
        def build(node:TreeNode,start:int,end:int):
            mid = int((start + end)/2)
            node.val = data[int((start + end)/2)]
            if start <= mid-1:
                t = TreeNode()
                node.left = t
                build(t,start,mid-1)
            if end >= mid+1:
                z = TreeNode()
                node.right = z
                build(z, mid + 1, end)
        get_info(root)
        a = TreeNode()
        build(a,0,len(data)-1)
        return a

