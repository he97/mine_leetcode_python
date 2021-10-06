from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        n = len(stones)
        m = sum(stones)
        count = 0

