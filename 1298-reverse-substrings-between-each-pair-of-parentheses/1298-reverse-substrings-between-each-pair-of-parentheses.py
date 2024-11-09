class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = []

        for x in s:
            if x == '(':
                stack.append(x)
            
            elif 'a' <= x <= 'z':
                stack.append(x)
            elif x == ')':
                temp = []
                while stack and stack[-1]!='(':
                    temp.append(stack.pop())
                stack.pop()
                stack.extend(temp)
        return "".join(stack)


        