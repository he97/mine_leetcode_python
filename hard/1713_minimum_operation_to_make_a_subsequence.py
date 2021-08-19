# 给你一个数组 target ，包含若干 互不相同 的整数，以及另一个
# 整数数组 arr ，arr 可能 包含重复元素。
# 
# 每一次操作中，你可以在 arr 的任意位置插入任一整数。比方说，
# 如果 arr = [1,4,1,2] ，那么你可以在中间添加 3 得到 [1,4,3,1,2] 。
# 你可以在数组最开始或最后面添加整数。
# 
# 请你返回 最少 操作次数，使得 target 成为 arr 的一个子序列。
# 
# 一个数组的 子序列 指的是删除原数组的某些元素（可能一个元素都不删除），
# 同时不改变其余元素的相对顺序得到的数组。
# 比方说，[2,7,4] 是 [4,2,3,7,2,1,4] 的子序列（加粗元素），
# 但 [2,4,2] 不是子序列。
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:

        operation_times: int = len(target)
        minimum_operation_time = operation_times

        for target_arr_index in range(0, len(target)):
            if target_arr_index + 1 > minimum_operation_time:
                return minimum_operation_time
            target_arr = target[target_arr_index: len(target)]
            operation_times = len(target)
            operation_times = self.get_operation_time(arr, operation_times, target_arr)
            if minimum_operation_time > operation_times:
                minimum_operation_time = operation_times
            print('第{0}循环结果是{1},此时的target子串是：{2}'.format(target_arr_index, operation_times, target_arr))
        return minimum_operation_time

    def get_operation_time(self, arr, operation_times, target_arr):
        first = False
        check = False
        search_arr = arr
        for target_index in range(0, len(target_arr)):
            for search_arr_index in range(0, len(search_arr)):
                # 匹配到了
                if target_arr[target_index] == search_arr[search_arr_index]:
                    if not first:
                        first = True
                    search_arr = search_arr[search_arr_index + 1: len(search_arr)]
                    check = True
                    operation_times -= 1
                    break
            if not check and first:
                # print('search_arr:', search_arr)
                # return operation_times
                check = False
        # return operation_times
        return operation_times


if __name__ == "__main__":
    demo = Solution()
    # [16,7,20,11,15,13,10,14,6,8]
    # ,[11,14,15,7,5,5,6,10,11,6]

    # [15,14,20,11,9,10,5,1,19,3]
    # [17,20,13,7,1,3,10,9,15,14]
#     result = demo.minOperations([15,14,20,11,9,10,5,1,19,3]
# ,[17,20,13,7,1,3,10,9,15,14])
    result = demo.get_operation_time(target_arr=[20, 11, 9, 10, 5, 1, 19, 3]
                                ,operation_times=10, arr=[17, 20, 13, 7, 1, 3, 10, 9, 15, 14])
    print(result)
