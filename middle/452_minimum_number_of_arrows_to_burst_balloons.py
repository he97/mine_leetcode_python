"""
首先根据开头的元素进行排序，根据points中元素x的第一个作为key
然后是从头开始进行融合，分为left与right
当下一个元素的start大于之前的right，则将之前的left与right作为一个飞镖。
元素需要取中间的并集
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        shot = 1
        # left = points[0][0]
        right = points[0][1]
        for i in range(len(points)):
            if points[i][0] > right:
                shot += 1
                # left = points[i][0]
                right = points[i][1]
            else:
                # left = min(points[i][0],right)
                right = min(points[i][1],right)
        return shot
