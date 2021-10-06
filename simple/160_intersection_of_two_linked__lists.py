# 给你两个单链表的头节点headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
#
# 图示两个链表在节点 c1 开始相交：
#
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 使用快慢指针
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == headB:
            return headA
        a = b = 0
        temp_a = headA
        temp_b = headB
        tag_a = True
        tag_b = True
        while True:
            if temp_a != temp_b:
                if temp_a.next is not None:
                    temp_a = temp_a.next
                elif temp_a.next is None and tag_a:
                    tag_a = False
                    temp_a = headB
                else:
                    return None
                if temp_b.next is not None:
                    temp_b = temp_b.next
                elif temp_b.next is None and tag_b:
                    tag_b = False
                    temp_b = headA
                else:
                    return None
            else:
                return temp_a



