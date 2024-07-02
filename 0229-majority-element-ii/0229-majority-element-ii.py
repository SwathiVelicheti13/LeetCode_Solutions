class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1 = ele2 = -1
        ct1 = ct2 = 0

        for val in nums:
            if ct1 == 0 and val!=ele2:
                ele1 = val
                ct1+=1
            elif ct1 !=0 and ct2 == 0 and val!=ele1:
                ele2 = val
                ct2+=1
            elif ele1 == val:
                ct1+=1
            elif ele2 == val:
                ct2+=1
            else:
                ct1 = ct1-1
                ct2 = ct2-1

        ct1 = ct2 = 0
        list1 = []
        for num in nums:
            if num == ele1:
                ct1+=1
            elif num == ele2:
                ct2+=1
        
        if ct1 > len(nums)/3:
            list1.append(ele1)
        if ct2 > len(nums)/3:
            list1.append(ele2)
        return list1

        