class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        ans = 0
        n = len(chars)

        while i<n:

            ele = chars[i]
            count=0

            while i<len(chars) and ele == chars[i]:
                count+=1
                i+=1

            chars[ans] = ele
            ans+=1
            if count>1:
                for x in str(count):
                    chars[ans] = x
                    ans+=1
        return ans