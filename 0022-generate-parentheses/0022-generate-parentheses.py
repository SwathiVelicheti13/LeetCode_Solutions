class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(open,close,s):
            if len(s) == 2*n:
                result.append(s)
               

            if open<n:
                helper(open+1,close,s+'(')
            
            if close<open:
                helper(open,close+1,s+')')

        helper(0,0,'')
        return result


            