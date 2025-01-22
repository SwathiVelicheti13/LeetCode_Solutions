class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dict1 = Counter(s)
        visited = set()
        stack = []

        for i in range(len(s)):
            dict1[s[i]] = dict1[s[i]] - 1

            if s[i] not in visited:
                while stack and stack[-1] > s[i] and dict1[stack[-1]]:
                    visited.remove(stack[-1])
                    stack.pop()
                
                visited.add(s[i])
                stack.append(s[i])
        return ''.join(stack)
                    


        
        