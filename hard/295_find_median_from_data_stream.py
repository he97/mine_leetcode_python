# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
#
# 例如，
#
# [2,3,4]的中位数是 3
#
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
#
# 设计一个支持以下两种操作的数据结构：
#
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-median-from-data-stream
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import math
from collections import defaultdict

import sortedcollections
from sortedcontainers import SortedList


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.right = 0
        self.left = 0
        self.d = SortedList()

    #     在设置左右两个吧，用于方便寻找中位数，以及记录中位数

    def addNum(self, num: int) -> None:
        num_ = self.d
        num_.add(num)
        n = len(self.d)
        c = self.d[self.left]
        # num_.add(0)
        # num_.add(1)
        # num_.add(10)
        # num_.add(1)
        if n == 1:
            self.right = self.left = 1
        else:
            if n % 2 == 1:
                if num > c:
                    self.right += 1
                elif num < c:
                    self.right += 1
                else:
                    self.right += 1
            else:
                if num > c:
                    self.left += 1
                elif num < c:
                    self.left += 1
                else:
                    self.left += 1

    def findMedian(self) -> float:
        return (self.d[self.left-1] + self.d[self.right-1]) / 2


demo = MedianFinder()
demo.addNum(40)
print(demo.findMedian())
demo.addNum(12)
print(demo.findMedian())
demo.addNum(16)
print(demo.findMedian())
demo.addNum(14)
print(demo.findMedian())
demo.addNum(35)
print(demo.findMedian())
demo.addNum(19)
print(demo.findMedian())
demo.addNum(6)
print(demo.findMedian())
demo.addNum(3)
print(demo.findMedian())
demo.addNum(1)
print(demo.findMedian())
demo.addNum(0)
print(demo.findMedian())
demo.addNum(0)
print(demo.findMedian())
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
