# 给你两个版本号 version1 和 version2 ，请你比较它们。
#
# 版本号由一个或多个修订号组成，各修订号由一个 '.' 连接。每个修订号由 多位数字 组成，可能包含 前导零 。每个版本号至少包含一个字符。修订号从左到右编号，下标从 0 开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，以此类推。例如，2.5.33 和 0.1 都是有效的版本号。
#
# 比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 忽略任何前导零后的整数值 。也就是说，修订号 1 和修订号 001 相等 。如果版本号没有指定某个下标处的修订号，则该修订号视为 0 。例如，版本 1.0 小于版本 1.1 ，因为它们下标为 0 的修订号相同，而下标为 1 的修订号分别为 0 和 1 ，0 < 1 。
#
# 返回规则如下：
#
# 如果version1>version2返回1，
# 如果version1<version2 返回 -1，
# 除此之外返回 0。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/compare-version-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = []
        b = []
        a = list(version1.split('.'))
        b = list(version2.split('.'))
        for i in range(len(a)):
            a[i] = int(a[i])
        for i in range(len(b)):
            b[i] = int(b[i])
        c = min(len(a), len(b))
        for i in range(c):
            if a[i] > b[i]:
                return 1
            elif a[i] < b[i]:
                return -1
        if c == len(b) and c < len(a):
            for i in range(c, len(a)):
                if a[i] != 0:
                    return 1
        elif c == len(a) and c < len(b):
            for i in range(c, len(b)):
                if b[i] != 0:
                    return -1
        return 0


demo = Solution()
print(demo.compareVersion('1.0.1', '1'))
print(demo.compareVersion(version1="1.01", version2="1.001"))
print(demo.compareVersion(version1="1.0", version2="1.0.0"))
print(demo.compareVersion(version1="0.1", version2="1.1"))
print(demo.compareVersion(version1="1.0.1", version2="1"))
print(demo.compareVersion(version1="7.5.2.4", version2="7.5.3"))
