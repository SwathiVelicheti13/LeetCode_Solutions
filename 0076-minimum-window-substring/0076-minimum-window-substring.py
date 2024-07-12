class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=r=0
        minlen = float('inf')
        Sind = -1
        dict1 = defaultdict(int)
        n = len(s)
        m = len(t)
        cnt = 0
        for i in range(m):
            dict1[t[i]]+=1
        
        while r<n:
            if dict1[s[r]]>0:
                cnt+=1
            dict1[s[r]] = dict1[s[r]]-1
            while cnt == m:
                if (r-l)+1 < minlen:
                    minlen = (r-l)+1
                    Sind = l
                
                dict1[s[l]] = dict1[s[l]]+1
                if dict1[s[l]] > 0:
                    cnt = cnt-1
                l+=1
            r+=1
        if Sind == -1:
            return ""
        else:
            substring = s[Sind:Sind+minlen]
            return substring

        