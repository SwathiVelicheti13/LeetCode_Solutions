class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        a =0 
        b= len(s)-1
        while a<b:
            s[a],s[b] =s[b],s[a]
            a=a+1
            b=b-1
        return s
        