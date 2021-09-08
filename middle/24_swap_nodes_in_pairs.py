# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        this = head
        if head is not None:
            this_next = this.next
        else:
            this_next = None
        temp = ListNode()
        if this_next is not None:
            head = this_next
        while this is not None and this_next is not None:
            if this_next.next is not None and this_next.next.next is not None:
                this.next = this_next.next.next
            else:
                this.next = this_next.next
            temp = this_next.next
            this_next.next = this
            this = temp
            if this is not None:
                this_next = this.next
            else:
                this_next = None
        return head

demo = Solution()
head_1 = ListNode(1)
head_2 = ListNode(2)
head_3 = ListNode(3)
head_4 = ListNode(4)
head_1.next = head_2
head_2.next = head_3
head_3.next = head_4
head = demo.swapPairs(head_1)
while head is not None:
    print(head.val)
    head = head.next
