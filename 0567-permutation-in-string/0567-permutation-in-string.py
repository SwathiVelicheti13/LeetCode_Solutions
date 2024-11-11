class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        s1Count = Counter(s1)

        wd_count = Counter(s2[:len1])

        if wd_count == s1Count:
            return True

        for i in range(len1,len2):
            wd_count[s2[i]]+=1
            wd_count[s2[i-len1]]-=1

            if wd_count[s2[i-len1]] == 0:
                del wd_count[s2[i-len1]]

            if wd_count == s1Count:
                return True
        return False

        