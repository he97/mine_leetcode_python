# 给定一颗根结点为 root 的二叉树，树中的每一个结点都有一个从 0 到 25 的值，分别代表字母 'a' 到 'z'：值 0 代表 'a'，值 1 代表 'b'，依此类推。
#
# 找出按字典序最小的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。
#
# （小贴士：字符串中任何较短的前缀在字典序上都是较小的：例如，在字典序上 "ab" 比 "aba" 要小。叶结点是指没有子结点的结点。）
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/smallest-string-starting-from-leaf
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def max_array(node: TreeNode, parent) -> list:
            left = []
            right = []
            if node.left is not None:
                left = max_array(node.left, node.val)
            if node.right is not None:
                right = max_array(node.right, node.val)
            left.append(node.val)
            right.append(node.val)
            n = len(left)
            m = len(right)
            if m == 1 and n > 1:
                return left
            elif m > 1 and n == 1:
                return right
            else:
                for i in range(min(m, n)):
                    if int(right[i]) < int(left[i]):
                        return right
                    elif int(right[i]) > int(left[i]):
                        return left
                i = min(m,n)
                while i < max(m,n):
                    if m > n:
                        if right[i] > parent:
                            return left
                        elif right[i] < parent:
                            return right
                        else:
                            i += 1
                    else:
                        if left[i] > parent:
                            return right
                        elif left[i] < parent:
                            return left
                        else:
                            i += 1
                if m > n:
                    return left
                else:
                    return right

        arr = max_array(root,-1)
        s = ''
        for i in range(len(arr)):
            s = s + chr(97 + arr[i])
        return s


demo = Solution()
# node_1 = TreeNode(0)
# node_2 = TreeNode(1)
# node_3 = TreeNode(2)
# node_4 = TreeNode(3)
# node_5 = TreeNode(4)
# node_6 = TreeNode(3)
# node_7 = TreeNode(4)
node_1 = TreeNode(2)
node_2 = TreeNode(2)
node_3 = TreeNode(1)
# node_4 = TreeNode(3)
node_5 = TreeNode(1)
node_6 = TreeNode(0)
# node_7 = TreeNode(4)
node_8 = TreeNode(0)
node_1.left = node_2
node_1.right = node_3
# node_2.left = node_4
node_2.right = node_5
node_3.left = node_6
# node_3.right = node_7
node_5.left = node_8
print(demo.smallestFromLeaf(node_1))
