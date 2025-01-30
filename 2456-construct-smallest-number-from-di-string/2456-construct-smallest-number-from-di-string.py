class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        num = 1
        res = []
        for pat in pattern:
            stack.append(num)
            num+=1

            if pat == 'I':
                while stack:
                    res.append(str(stack.pop()))

        stack.append(num)
        while stack:
            res.append(str(stack.pop()))
        
        return ''.join(res)
                    
