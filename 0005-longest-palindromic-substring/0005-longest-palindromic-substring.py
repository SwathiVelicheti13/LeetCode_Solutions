class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(l,r):
            while l >= 0 and r<len(s) and s[l] == s[r]:
                l=l-1
                r+=1
            return s[l+1:r]

        longPalin = ""
        for i in range(len(s)):
            odd_value = expand(i,i)
            even_value = expand(i,i+1)

            longPalin = max(longPalin,odd_value,even_value, key=len)
        return longPalin



        