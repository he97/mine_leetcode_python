# 输入两个链表，找出它们的第一个公共节点。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# from Cython.Compiler.ExprNodes import ListNode




class Solution:
    def find_intersection_node(self, headA, headB):
        result: ListNode = None
        tag = False
        if headA.next is not None and headB.next is not None:
            result, tag = Solution.find_intersection_node(headA=headA.next, headB=headB.next)
        if headA is not None and headB is not None and not tag:
            if headA.val == headB.val:
                return headA, tag
            else:
                return result, True

    # 递归这个数组 从最后一个数到
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        temp_a: ListNode = headA
        temp_b: ListNode = headB
        count_a = count_b = 0
        check_num = 0
        while temp_a is not None:
            count_a += 1
            temp_a= temp_a.next
        while temp_b is not None:
            count_b += 1
            temp_b = temp_b.next
        if count_a > count_b:
            remove_num = count_a - count_b
            check_num = count_b
            while remove_num > 0:
                headA = headA.next
                remove_num -=1
        else:
            check_num = count_a
            remove_num = count_b - count_a
            while remove_num > 0:
                headB = headB.next
                remove_num -= 1
        a = self.find_intersection_node(headA, headB)

        # if headA.next is None and headB.next is None:

demo = Solution()
# a_1 = a_2 = a_3 = a_4 = a_5 = ListNode()
# b_1 = b_2 = b_3 = b_4 = b_5 = b_6 = ListNode()
# a_1 = ListNode(4)
# a_2 = ListNode(1)
# a_3 = ListNode(8)
# a_4 = ListNode(4)
# a_5 = ListNode(5)
a_1 = ListNode(2)
a_2 = ListNode(6)
a_3 = ListNode(4)
# a_4 = ListNode(2)
# a_5 = ListNode(4)
a_1.next = a_2
a_2.next = a_3
# a_3.next = a_4
# a_4.next = a_5


# b_1 = ListNode(5)
# b_2 = ListNode(0)
# b_3 = ListNode(1)
# b_4 = ListNode(8)
# b_5 = ListNode(4)
# b_6 = ListNode(5)
b_1 = ListNode(1)
b_2 = ListNode(5)
# b_3 = ListNode(4)
# b_4 = ListNode(8)
# b_5 = ListNode(4)
# b_6 = ListNode(5)
b_1.next = b_2
# b_2.next = b_3



demo.getIntersectionNode(headA=a_1, headB=b_1)


































