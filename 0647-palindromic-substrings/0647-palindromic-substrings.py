class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(i,j,s):
            count = 0
            while i>=0 and j<len(s) and s[i]==s[j]:
                count+=1
                i = i-1
                j = j+1
            return count
        
        i = 0
        count = 0
        n = len(s)
        while i<len(s):
            count+=expand(i,i,s)
            count+=expand(i,i+1,s)
            i+=1
        return count

        
       