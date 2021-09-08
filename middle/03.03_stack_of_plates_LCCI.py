# 堆盘子。设想有一堆盘子，堆太高可能会倒下来。因此，在现实生活中，盘子堆到一定高度时，我们就会另外堆一堆盘子。请实现数据结构SetOfStacks，模拟这种行为。SetOfStacks应该由多个栈组成，并且在前一个栈填满时新建一个栈。此外，SetOfStacks.push()和SetOfStacks.pop()应该与普通栈的操作方法相同（也就是说，pop()返回的值，应该跟只有一个栈时的情况一样）。 进阶：实现一个popAt(int index)方法，根据指定的子栈，执行pop操作。
#
# 当某个栈为空时，应当删除该栈。当栈中没有元素或不存在该栈时，pop，popAt 应返回 -1.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/stack-of-plates-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import math


class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0 or len(self.stack[-1]) == self.cap:
            if self.cap > 0:
                a = [val]
                self.stack.append(a)
        else:
            self.stack[-1].append(val)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            if len(self.stack[-1]) > 1:
                a = self.stack[-1].pop()
            else:
                a = self.stack[-1].pop()
                self.stack.pop()
            return a

    def popAt(self, index: int) -> int:
        a = len(self.stack)
        if index >= a:
            return -1
        else:
            c = self.stack[index].pop()
            if len(self.stack[index]) == 0:
                del self.stack[index]
            return c


demo = StackOfPlates(1)
print(demo.push(1))
print(demo.push(2))
print(demo.popAt(1))
print(demo.pop())
print(demo.pop())
# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)
