class Solution:
    def smallestSubsequence(self, s: str) -> str:
        d = Counter(s)
        visited = set()
        stack = []

        for i in range(len(s)):
            d[s[i]] = d[s[i]] - 1

            if s[i] not in visited:
                while stack and stack[-1] > s[i] and d[stack[-1]]:
                    visited.remove(stack[-1])
                    stack.pop()
                
                visited.add(s[i])
                stack.append(s[i])
        return ''.join(stack)