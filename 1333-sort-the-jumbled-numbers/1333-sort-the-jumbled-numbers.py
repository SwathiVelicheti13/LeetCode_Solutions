class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []
        for i,n in enumerate(nums):
            mapped_n = 0
            for k in str(n):
                mapped_n *= 10
                mapped_n += mapping[int(k)]
                #print(new_num)
            #print(new_num)
            pairs.append((mapped_n,i))
        pairs.sort()
        return [nums[p[1]] for p in pairs]
        