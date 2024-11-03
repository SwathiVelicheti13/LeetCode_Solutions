class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        list1 = [0]
        def helper(x,target,list1,currSum):
            if x >= len(candidates):
                return
            if currSum == target:
                res.append(list1[:])
                
                return
            if currSum < target:
                list1.append(candidates[x])
                currSum+=candidates[x]
                helper(x,target,list1,currSum)
                currSum= currSum - list1.pop()  
            helper(x+1,target,list1,currSum)
        helper(0,target,[],0)
        return res
                
        