# 给定一个二叉树（具有根结点root），一个目标结点target，和一个整数值 K 。
#
# 返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 给点根节点 与 目标节点
    #
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 进行递归算法
        # depth = 1
        selected = set([])
        if root != target:
            remain, selected = self.search_distance_k(root=root, target=target, depth=k)
        else:
            selected = self.below_distance_k(root, k)
        # print('remain:{0},set:{1}'.format(remain, set))
        print(list(selected))
        if k != 0:
            selected.discard(int(target.val))
        return list(selected)

    def search_distance_k(self, root: TreeNode, target: TreeNode, depth: int):
        selected_node = set([])
        temp: set([])
        # remain = 0
        if root is None:
            return -1, selected_node
        if root == target:
            return depth-1, self.below_distance_k(root, depth)
        if root.left is not None:
            # remain为递归回来的,应该向下查多少层,temp为上层返回的结点
            remain, temp = self.search_distance_k(root.left, target, depth)
            # print('remain的值为:{0}，此时的节点值是:{1}'.format(remain, root.val))
            selected_node = selected_node.union(temp)
            if remain >= 0:
                if remain == 0:
                    selected_node.add(root.val)
                elif remain > 0 and root.right is not None:
                    selected_node = selected_node.union(self.below_distance_k(root.right, remain-1))
                if len(selected_node) >= 0:
                    return remain-1, selected_node
        if root.right is not None:
            # remain为递归回来的,应该向下查多少层,temp为上层返回的结点
            remain, temp = self.search_distance_k(root.right, target, depth)
            # print('remain的值为:{0}，此时的节点值是:{1}'.format(remain, root.val))
            selected_node = selected_node.union(temp)
            if remain >= 0:
                if remain == 0:
                    selected_node.add(root.val)
                elif remain > 0 and root.left is not None:
                    selected_node = selected_node.union(self.below_distance_k(root.left, remain-1))
                if len(selected_node) >= 0:
                    return remain-1, selected_node
        return -1, selected_node
        # print('remain的值为:{0}，此时的节点值是:{1}'.format(remain, root.val))
        # return remain-1, selected_node
        # if root != target:
        #
        #     # remain返回的是向上的，递减
        #     remain, temp = self.search_diatance_k(root.left, target, depth + 1)
        #     self.below_distance_k(root, remain)
        #     # 这块的dataset有问题
        #     remain, dataset = self.search_diatance_k(root.right, target, depth + 1)
        #     self.below_distance_k(root, remain)

    # 返回向下 距离为k的所有节点
    @staticmethod
    def below_distance_k(root: TreeNode, k: int) -> {int}:
        # set 记录相隔k距离的值
        s = set([])
        # 用数组记录树
        # tree = []
        if k == 0:
            s.add(root.val)
            return s
        # 用来进行层次遍历
        depth = 1
        this_level = [root]
        next_level = []
        # tree.append(root)
        i = 0
        # 对树进行层次遍历
        while this_level[i] is not None:
            if this_level[i].left:
                # tree.append(this_level[i].left)
                next_level.append(this_level[i].left)
                if k == depth:
                    s.add(this_level[i].left.val)
            # else:
            # tree.append(None)
            if this_level[i].right:
                # tree.append(this_level[i].right)
                next_level.append(this_level[i].right)
                if k == depth:
                    s.add(this_level[i].right.val)
            # else:
            #     tree.append(None)
            # 到了this_level 最后一个元素
            if i == len(this_level) - 1:
                if k <= depth:
                    break
                depth += 1
                i = 0
                if len(next_level) > 0:
                    this_level = next_level
                    next_level = []
                else:
                    return s
            else:
                i += 1
        return s



demo = Solution()
node_0 = TreeNode(0)
node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)
node_7 = TreeNode(7)
node_8 = TreeNode(8)

# node_3.left = node_5
# node_3.right = node_1
# node_5.left = node_6
# node_5.right = node_2
# node_1.left = node_0
# node_1.right = node_8
# node_2.left = node_7
# node_2.right = node_4
node_0.left = node_1
node_1.right = node_2
node_1.left = node_3
# node_1.right = node_2
# node_2.right = node_3
# node_3.right = node_4

demo.distanceK(node_0, target=node_2, k=1)
# demo.search_distance_k(root=node_1,target=node_2,depth=2)
# print(demo.below_distance_k(node_3, 0))