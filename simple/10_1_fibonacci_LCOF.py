class Solution:
    def fib(self, n: int) -> int:
        a = []
        if n >= 0:
            a.append(0)
        if n >= 1:
            a.append(1)
        for i in range(2,n+1):
            a.append((a[-1]+a[-2])%(10**9+7))
        return a[n]

demo = Solution()
print(demo.fib(45))