class Solution:
    def checkValidString(self, s: str) -> bool:
        s = list(s)
        stack = []
        left_brackets_index = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
                left_brackets_index.append(len(stack)-1)
                # left_brackets += 1
            elif s[i] == '*':
                stack.append('*')
                # star += 1
            elif s[i] == ')':
                if len(left_brackets_index) > 0:
                    stack.pop(left_brackets_index[-1])
                    left_brackets_index.pop()
                else:
                    if len(stack) > 0:
                        stack.pop()
                    else:
                        return False
        star = 0
        # 保证最后已经有一个星号了
        for i in range(len(stack)-1,-1,-1):
            if stack[i] == '(':
                if star > 0:
                    star -= 1
                else:
                    return False
            else:
                star += 1
        return True



demo = Solution()
print(demo.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
print(demo.checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))