# 你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/pattern-matching-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 输入： pattern = "abba", value = "dogcatcatdog"
# 输出： true
class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        d = {'a': 0, 'b': 0}
        v = list(value)
        n = len(v)
        p = list(pattern)
        for i in p:
            d[i] += 1
        if n == 0 and (d['a'] == 0 or d['b'] == 0):
            return True
        elif n == 0 and d['a'] > 0 and d['b'] > 0:
            return False
        if d['a'] == 0 or d['b'] == 0:
            c = max(d['a'], d['b'])
            if n % c != 0:
                return False
            else:
                d = n // c
                for k in range(d, n, d):
                    if v[0:d] != v[k:k + d]:
                        return False
                return True
        a_max = n // d['a'] + 1
        a = 0

        while a < a_max:
            if (n - a*d['a']) % d['b'] == 0:
                b = (n - a*d['a']) // d['b']
                tag = True
                pre_a = -1
                pre_b = -1
                j = 0
                for index in range(len(p)):
                    if p[index] == 'a':
                        if pre_a == -1:
                            pre_a = j
                        else:
                            if v[pre_a:pre_a+a] != v[j:j+a]:
                                tag = False
                                break
                        j += a
                    if p[index] == 'b':
                        if pre_b == -1:
                            pre_b = j
                        else:
                            if v[pre_b:pre_b+b] != v[j:j+b]:
                                tag = False
                                break
                        j += b
                if tag:
                    return True
            a += 1
        return False


demo = Solution()
print(demo.patternMatching("bbb"
,"xxxxxx"))