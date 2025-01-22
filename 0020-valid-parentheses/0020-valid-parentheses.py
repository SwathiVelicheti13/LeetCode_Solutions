class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for brac in s:
            if brac == '[' or brac == '(' or brac == '{':
                stack.append(brac)

            elif len(stack)>0 and ((brac == ']' and stack[-1] == '[')  or (brac == ')' and stack[-1] =='(') or (brac == '}' and stack[-1] == '{')):
                stack.pop()

            elif brac == ']' or brac == ')' or brac == '}' :
                return False
        if len(stack)>0:
            return False
        return True


        