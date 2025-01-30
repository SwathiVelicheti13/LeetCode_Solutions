class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1 for _ in range(len(s)+1)]

        def recursiveDecode(ind):
            if ind == len(s):
                return 1

            if s[ind] == '0':
                return 0
            
            if dp[ind]!=-1:
                return dp[ind]
            one_digit = recursiveDecode(ind+1)

            two_digit = 0
            if ind+1<len(s) and int(s[ind:ind+2])<=26:
                two_digit = recursiveDecode(ind+2)

            dp[ind]=one_digit+two_digit
            return dp[ind]
        return recursiveDecode(0)

            

           