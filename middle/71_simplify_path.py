"""
首先是使用栈，然后是使用
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        l = []
        point_count = 0
        d = path.split('/')
        s = ''
        for i in d:
            if len(i) != 0:
                if i == '..':
                    if len(l) > 0:
                        l.pop()
                elif i == '.' or i == '':
                    pass
                else:
                    l.append(i)
        if len(l) > 0:
            for i in l:
                s += '/' + i
        else:
            s = '/'
        return s
