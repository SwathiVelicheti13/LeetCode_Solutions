class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def expand_center(l,r):
            count = 0
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l=l-1
                r=r+1
            return count

        total_palindrome = 0
        for i in range(len(s)):
            total_palindrome+=expand_center(i,i)

            total_palindrome+=expand_center(i,i+1)
        
        return total_palindrome



        