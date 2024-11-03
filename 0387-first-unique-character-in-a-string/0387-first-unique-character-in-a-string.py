class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = defaultdict(int)
        for i in s:
            dict1[i]+=1
        
        for i in s:
            if dict1[i] == 1:
                return s.index(i)
        return -1

        