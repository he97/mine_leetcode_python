from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        a = [0] * 26
        l = list(s)
        d = []
        maximum = 1
        for i in range(len(l)):
            if a[ord(l[i]) - 97] == 0:
                a[ord(l[i]) - 97] = maximum
                maximum += 1
                d.append(1)
            else:
                c = a[ord(l[i]) - 97]
                d[c - 1] += 1
                if c < maximum - 1:
                    d[c - 1] = sum(d[c - 1:])
                    for k in range(len(a)):
                        if a[k] > c:
                            a[k] = c
                    maximum = c + 1
                    d = d[:c]
        return d
