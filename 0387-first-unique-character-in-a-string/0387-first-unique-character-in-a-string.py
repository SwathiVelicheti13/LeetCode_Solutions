class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = defaultdict(int)
        for i in s:
            dict1[i]+=1
        
        for key, val in dict1.items():
            if val == 1:
                return s.index(key)
        return -1
        
        
        