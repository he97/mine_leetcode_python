class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        a = sum(chalk)
        b = k%a
        for i in range(len(chalk)):
            if b >= chalk[i]:
                b -= chalk[i]
            else:
                return i
        return len(chalk)-1