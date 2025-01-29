class Solution:
    def compress(self, chars: List[str]) -> int:
        ind = 0
        i = 0
        n = len(chars)
        while i<n:
            ele = chars[i]
            count = 0
            while i<len(chars) and chars[i] == ele:
                count+=1
                i+=1
            chars[ind] = ele
            ind+=1
            if count>1:  
                for m in str(count):
                    chars[ind] = m
                    ind+=1
        return ind


            

        