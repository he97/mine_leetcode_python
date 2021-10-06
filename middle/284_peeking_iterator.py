# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
from collections import Iterator


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.a = iterator
        self.temp = -1
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.temp == -1:
            self.temp = self.a.next()
        return self.temp
    def next(self):
        """
        :rtype: int
        """
        if self.temp != -1:
            x = self.temp
            self.temp = -1
            return x
        else:
            return self.a.next()
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.temp != -1:
            return True
        else:
            return self.a.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
iter = PeekingIterator([1,2,3])
while iter.hasNext():
    val = iter.peek()   # Get the next element but not advance the iterator.
    # iter.next()         # Should return the same value as [val].
    print(val)
    print(iter.next())
