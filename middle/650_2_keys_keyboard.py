# 最初记事本上只有一个字符 'A' 。你每次可以对这个记事本进行两种操作：
#
# Copy All（复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。
# Paste（粘贴）：粘贴 上一次 复制的字符。
# 给你一个数字n ，你需要使用最少的操作次数，在记事本上输出 恰好n个 'A' 。返回能够打印出n个 'A' 的最少操作次数。
#
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/2-keys-keyboard
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1   :
            return 0
        # 初始状态
        a = 1
        count = 1
        c = 1
        # c: copy的数值
        # a: 总数值
        # 字符串：上次执行的操作
        l = [[c, a, 'c']]
        while l is not None and True:
            count += 1
            temp = []
            # m = max(l,key=lambda x:(x[0], x[1]))
            for i in l:
                if i[2] == 'c':
                    if i[1] + i[0] < n:
                        temp.append([i[0], i[1] + i[0], 'p'])
                    elif i[1] + i[0] == n:
                        return count
                elif i[2] == 'p':
                    if i[1] + i[0] < n:
                        temp.append([i[0], i[1] + i[0], 'p'])
                    elif i[1] + i[0] == n:
                        return count
                    temp.append([i[1], i[1], 'c'])
            l = temp

