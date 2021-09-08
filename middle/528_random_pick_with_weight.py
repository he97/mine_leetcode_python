import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.count = 0
        self.data = []
        for i in w:
            self.data.append(self.count + i)
            self.count += i

    def pickIndex(self) -> int:
        ran = random.randint(1, self.count)
        low = 0
        high = len(self.data)
        mid = int((low+high)/2)
        while low < high:
            if self.data[mid] < ran:
                low = mid + 1
                mid = int((low+high)/2)
            elif self.data[mid] > ran:
                if self.data[mid-1] < ran:
                    return mid
                else:
                    high = mid - 1
                    mid = int((low + high) / 2)
            else:
                return mid
        return low

# Your Solution object will be instantiated and called as such:
w=[3,14,1,7]
obj = Solution(w)
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
print(obj.pickIndex())
