class Solution:
    def minimumMoves(self, s: str) -> int:
        l = list(s)
        count = 0
        n = len(s)
        for i in range(n):
            if l[i] == 'X':
                for j in range(3):
                    if (i+j) < n:
                        l[i + j] = 'O'
                count += 1
        return count
