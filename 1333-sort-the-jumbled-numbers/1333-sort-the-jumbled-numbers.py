class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []
        mapped_n = 0

        for ind,val in enumerate(nums):
            mapped_n = 0

            for k in str(val):
                mapped_n = mapped_n*10
                mapped_n+=mapping[int(k)]
            
            pairs.append((mapped_n,ind))
        pairs.sort()

        return [nums[p[1]] for p in pairs]

                