class Solution:
    def countSegments(self, s: str) -> int:
        c = list(s)
        count = 0
        tag = False
        for i in c:
            if i == ' ' and tag:
                count += 1
                tag = False
            elif i != ' ':
                tag = True
        if count != 0 and tag:
            return count + 1
        elif tag:
            return count + 1
        return count
