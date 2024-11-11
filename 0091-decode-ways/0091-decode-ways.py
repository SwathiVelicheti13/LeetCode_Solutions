class Solution:
    def numDecodings(self, s: str) -> int:


        if len(s)==0:
            return 0
        if s[0]=='0':
            return 0

        dp = [0 for _ in range(len(s)+1)]

        dp[0] = 1
        dp[1] = 1

        for i in range(2,len(dp)):
            if int(s[i-1])!=0:
                dp[i]+=dp[i-1]
            
            two = s[i-2:i]

            if 10<=int(two)<=26:
                dp[i]+=dp[i-2]
        print(dp)
        return dp[len(s)]


        