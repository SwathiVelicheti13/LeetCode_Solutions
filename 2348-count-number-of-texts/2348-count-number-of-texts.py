class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n = len(pressedKeys)
        dp = [0 for _ in range(len( pressedKeys)+1)]

        dp[0] = 1

        for i in range(1,n+1):
            dp[i] = dp[i-1]

            if i-2>=0 and  pressedKeys[i-2] ==  pressedKeys[i-1]:
                dp[i]+=dp[i-2]
            
            if i-3>=0 and pressedKeys[i-3] == pressedKeys[i-2] == pressedKeys[i-1]:
                dp[i]+=dp[i-3]
            
            if i-4>=0 and pressedKeys[i-4] == pressedKeys[i-3] == pressedKeys[i-1] == pressedKeys[i-2] and pressedKeys[i-1] in ['7','9']:
                dp[i]+=dp[i-4]
            
            dp[i] = dp[i] % (pow(10,9)+7)
        return dp[-1]