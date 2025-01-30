class Solution:
    def compress(self, chars: List[str]) -> int:
        ind = 0
        i = 0
        while i < len(chars):
            ele = chars[i]
            count = 0
            while i<len(chars) and chars[i] == ele:
                count+=1
                i+=1
            
            chars[ind] = ele
            ind+=1

            if count>1:
                for x in str(count):
                    chars[ind] = x
                    ind+=1
        return ind

