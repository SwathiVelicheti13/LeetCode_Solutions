class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s)<=1:
            return False
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            
            elif len(stack) > 0 and ((char == ')' and stack[-1] == '(') or (char == ']' and stack[-1] == '[') or (char == '}' and stack[-1] == '{')):
                stack.pop()
            elif (char == ')' or char == ']' or char == '}'):
                return False



        if stack:
            return False
        return True


        