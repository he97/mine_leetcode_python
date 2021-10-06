class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        l = list(s)
        ll = []
        result = ''
        for i in range(len(l)):
            if l[i] != '-':
                ll.append(str(l[i]).upper())
        a = len(ll)
        b = a // k
        c = a % k
        if c > 0:
            result += ''.join(ll[:c])
        else:
            result += ''.join(ll[:k])
            c+=k
        while c < a:
            result += '-'
            result += ''.join(ll[c:c+k])
            c+=k
        return result
