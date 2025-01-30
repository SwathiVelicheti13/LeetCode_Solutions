class Solution:
    def numDecodings(self, s: str) -> int:
        

        if len(s) == 0:
            return 0 

        if s[0] == '0':
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


        # dp = [-1 for _ in range(len(s)+1)]

        # def recursiveDecode(ind):
        #     if ind == len(s):
        #         return 1

        #     if s[ind] == '0':
        #         return 0
            
        #     if dp[ind]!=-1:
        #         return dp[ind]
        #     one_digit = recursiveDecode(ind+1)

        #     two_digit = 0
        #     if ind+1<len(s) and int(s[ind:ind+2])<=26:
        #         two_digit = recursiveDecode(ind+2)

        #     dp[ind]=one_digit+two_digit
        #     return dp[ind]
        # return recursiveDecode(0)

            

           