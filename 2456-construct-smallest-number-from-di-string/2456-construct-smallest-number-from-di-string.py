class Solution:
    def smallestNumber(self, pattern: str) -> str:
        m = 0
        ans =[1]

        for ch in pattern:
            if ch == 'I':
                m = ans[-1]+1
                while m in ans:
                    m+=1
                ans.append(m)
            else:
                ans.append(ans[-1])
                for x in range(len(ans)-1,0,-1):
                    if ans[x] == ans[x-1]:
                        ans[x-1] = ans[x-1]+1
        ans = list(map(str,ans))
        return ''.join(ans)

        