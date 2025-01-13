from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq_p = Counter(p)
        freq_s = Counter()

        l = 0
        res = []
        for r in range(len(s)):
            freq_s[s[r]]+=1
            if ((r-l)+1) > len(p):
                freq_s[s[l]] = freq_s[s[l]] - 1
                if freq_s[s[l]] == 0:
                    del freq_s[s[l]]
            
                l+=1
            if freq_s == freq_p:
                res.append(l)
        return res

