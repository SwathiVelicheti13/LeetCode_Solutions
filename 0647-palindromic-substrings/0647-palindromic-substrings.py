class Solution:
    def countSubstrings(self, s: str) -> int:
        

        def expand(i,j):
            count = 0
            while i>=0 and j<len(s) and s[i] == s[j]:
                count+=1
                i = i-1
                j+=1
            return count
        
        total = 0
        for i in range(len(s)):
            odd_count = expand(i,i)
            even_count = expand(i,i+1)

            total+=(odd_count+even_count)
        return total    