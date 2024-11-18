class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ans = []
        list1 = []
        def helper(ind):
            if ind == len(s):
                ans.append(list1[:])
                return 

            for val in range(ind,len(s)):
                if s[ind:val+1] == s[ind:val+1][::-1]:
                    list1.append(s[ind:val+1])
                    helper(val+1)
                    list1.pop()
        helper(0)
        return ans

        