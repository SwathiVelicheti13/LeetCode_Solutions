from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)

        nums_sorted = sorted(nums,reverse=True)

        sorted_nums = sorted(nums_sorted,key = lambda x:freq[x])

        return sorted_nums
           
        
            
        
        # check values with same freq

    



        