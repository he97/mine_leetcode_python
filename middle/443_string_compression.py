# 给你一个字符数组 chars ，请使用下述算法压缩：
#
# 从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：
#
# 如果这一组长度为 1 ，则将字符追加到 s 中。
# 否则，需要向 s 追加字符，后跟这一组的长度。
# 压缩后得到的字符串 s 不应该直接返回 ，
# 需要转储到字符数组 chars 中。
# 需要注意的是，如果组长度为 10 或 10 以上，
# 则在 chars 数组中会被拆分为多个字符。
#
# 请在 修改完输入数组后 ，返回该数组的新长度。
#
# 你必须设计并实现一个只使用常量额外空间的算法来解决此问题。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/string-compression
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        i = 0

        def insert_data(k: int, inner_index: int) -> int:
            if k >= 10:
                inner_index = insert_data(int(k / 10), inner_index)
                data = k % 10
                chars[inner_index] = str(data)
            elif k > 0:
                data = k % 10
                chars[inner_index] = str(data)
            return inner_index + 1

        while i < len(chars):
            temp = chars[i]
            chars[index] = temp
            index += 1
            j = i + 1
            while j < len(chars):
                if chars[j] == temp:
                    j += 1
                else:
                    break
            times = j - i
            if times >= 2:
                index = insert_data(times, index)
            i = j
        return index


demo = Solution()
print(demo.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
