class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def processString(string):
            stack = []

            for char in string:
                if char == '#' and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            
            return stack
        
        return processString(s) == processString(t)


        