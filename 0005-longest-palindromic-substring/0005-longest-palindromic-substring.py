class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_center(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left=left-1
                right+=1
            return s[left+1:right]

        long_palindrome = ""
        for i in range(len(s)):
            l = expand_center(i,i)
            r = expand_center(i,i+1)

            long_palindrome = max(long_palindrome,l,r ,key=len)
        return long_palindrome
        