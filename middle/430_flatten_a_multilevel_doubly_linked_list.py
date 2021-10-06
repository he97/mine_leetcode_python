# 多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。
#
# 给你位于列表第一级的头节点，请你扁平化列表，使所有结点出现在单级双链表中。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# """
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# """

class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        def search(h: 'Node'):
            if h is not None:
                print(h.val)
                if h.child is not None:
                    temp = h.next
                    nex = search(h.child)
                    h.next = h.child
                    h.child.prev = h
                    h.child = None
                    nex.next = temp
                    if temp is not None:
                        temp.prev = nex
                        c = search(temp)
                        return c
                    return nex
                elif h.next is not None:
                    a = search(h.next)
                    return a
                elif h.next is None:
                    return h


        search(head)
        return head
