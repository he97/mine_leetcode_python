# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        point_1 = None
        point_2 = None
        point_2 = head
        temp = point_2
        if head is None or head.next is None:
            return head
        while point_2.next is not None:
            # 前后相等
            if point_2.next.val == point_2.val:
                point_2 = point_2.next
            #     前后不相等
            else:
                if temp is point_2:
                    if point_1 is None:
                        head = temp
                    point_1 = temp
                    point_2 = temp = point_2.next
                elif temp is not point_2:
                    if point_1 is not None:
                        point_1.next = point_2.next
                    point_2 = temp = point_2.next
        if point_2 is not temp:
            if point_1 is not None:
                point_1.next = point_2.next
            elif point_1 is None:
                return None
        else:
            if point_1 is None:
                head = temp
        return head
