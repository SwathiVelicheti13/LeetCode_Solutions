class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
        num = 1  # Start with 1
        
        for ch in pattern:
            stack.append(num)
            num += 1
            
            if ch == 'I':
                while stack:
                    result.append(str(stack.pop()))
        
        # Push the last remaining number
        stack.append(num)
        while stack:
            result.append(str(stack.pop()))

        return "".join(result)
       