"""
构建个插分数组，然后
"""
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        a = []
        prev = 0
        for i in releaseTimes:
            a.append(i - prev)
            prev = i
        c = max(a)
        z = filter(lambda x: a[x] == c, range(len(releaseTimes)))
        return max(keysPressed[i] for i in z)
