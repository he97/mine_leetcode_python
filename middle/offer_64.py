class Solution:
    def sumNums(self, n: int) -> int:
        def get_res(n):
            return n and n + get_res(n - 1)

        return get_res(n)

demo = Solution()
print(demo.sumNums(1000))