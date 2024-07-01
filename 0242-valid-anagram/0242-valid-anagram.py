class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        for i in s:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i]+=1
        count=0
        for i in t:
            if i not in dict1:
                return False
            else:
               dict1[i] = dict1[i]-1
        
        for val in dict1.values():
            if val !=0:
                return False
        return True

            

        