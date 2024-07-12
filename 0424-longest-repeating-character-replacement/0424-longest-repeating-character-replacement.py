class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=r=0
        maxf = 0
        dict1 = defaultdict(int)
        maxlen = 0

        while r<len(s):
            dict1[s[r]]+=1
            maxf = max(maxf,dict1[s[r]])
            while ((r-l)+1)-maxf>k:
                dict1[s[l]] =  dict1[s[l]]-1
                if  dict1[s[l]] == 0:
                    dict1.pop(s[l])
                l+=1
            changes =  ((r-l)+1)-maxf
            if changes<=k:
                len1 = (r-l)+1
                maxlen=max(len1,maxlen)
            r+=1
        return maxlen
        