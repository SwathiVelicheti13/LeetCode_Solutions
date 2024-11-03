class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def helper(openC,closeC,s):
            if len(s) == 2*n:
                res.append(s)
                return
            if openC<n:
                helper(openC+1,closeC,s+'(')

            if openC>closeC:
                helper(openC,closeC+1,s+')')
                
        helper(0,0,'')
        return res
        


        