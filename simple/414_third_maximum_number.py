from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        array = [-float('inf')] * 3
        nums = list(set(nums))
        for i in range(len(nums)):
            if nums[i] > array[-1]:
                for j in range(3):
                    if nums[i] > array[j]:
                        if j < 2:
                            array[j + 1:] = array[j:2]
                        array[j] = nums[i]
                        break
        if array[-1] != -float('inf'):
            return int(array[-1])
        else:
            return int(array[0])


demo = Solution()
print(demo.thirdMax([1,2]))
print(
    demo.thirdMax([3, 2, 1])
)
