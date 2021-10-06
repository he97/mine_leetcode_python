# 给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。
#
# 每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。
#
# 这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。
#
# 返回一个符合上述规则的链表的列表。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/split-linked-list-in-parts
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for singly-linked list.
import math
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        temp = head
        n = 0
        while temp is not None:
            n += 1
            temp = temp.next
        a = math.floor(n / k)
        b = n % k
        print("a:{0},b:{1}".format(a,b))
        result = []
        temp = head
        for i in range(b):
            z = a + 1
            result.append(temp)
            while z > 1:
                if temp is not None:
                    temp = temp.next
                else:
                    break
                z -= 1
            if temp is None or temp.next is None:
                for j in range(b, k):
                    result.append(None)
                return result
            elif temp is not None and temp.next is not None:
                v = temp.next
                temp.next = None
                temp = v
        for i in range(b, k):
            z = a
            result.append(temp)
            while z > 1:
                if temp is not None:
                    temp = temp.next
                else:
                    temp = None
                z -= 1
            if temp is None or temp.next is None:
                for j in range(i+1, k):
                    result.append(None)
                return result
            elif temp is not None and temp.next is not None:
                v = temp.next
                temp.next = None
                temp = v
        return result
