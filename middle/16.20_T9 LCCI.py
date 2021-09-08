# 在老式手机上，用户通过数字键盘输入，
# 手机将提供与这些数字相匹配的单词列表。
# 每个数字映射到0至4个字母。
# 给定一个数字序列，实现一个算法来返回匹配单词的列表。
# 你会得到一张含有有效单词的列表
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/t9-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from collections import defaultdict
from typing import List


class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        d = defaultdict(int)
        value = 6
        number = []
        put = int(num)
        output = []
        # to r
        for i in range(97, 115):
            d[chr(i)] = int(value / 3)
            value += 1
        d['s'] = 7
        for i in range(116, 122):
            d[chr(i)] = int(value / 3)
            value += 1
        d['z'] = 9
        # 改进的空间就是不用计算temp，从第一个数开始对比，将num化为数组。
        for i in range(0, len(words)):
            data = list(words[i])
            temp = 0
            for j in range(0, len(data)):
                temp = temp * 10 + d[data[j]]
            number.append(temp)
        for i, value in enumerate(number):
            if value == put:
                output.append(words[i])
        return output


demo = Solution()
print(demo.getValidT9Words(num="8733", words=["tree", "used"]))
print(demo.getValidT9Words(num = "2", words = ["a", "b", "c", "d"]))
