class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind1 = 0
        ind2 = len(numbers)-1
        
        while ind1<ind2:
            sum1 = numbers[ind1]+numbers[ind2]
            if sum1> target:
                ind2 = ind2-1
            elif sum1<target:
                ind1 = ind1+1
            else:
                return (ind1+1,ind2+1)
        
