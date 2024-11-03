class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoHash={}

        pfSum = 0

        for val in range(0,len(nums)):
            pfSum=nums[val]
            Needed = target - pfSum
            if Needed in twoHash:
                return [twoHash[Needed],val]
            twoHash[pfSum] = val
        print(pfSum)
        return [0,0]

            

