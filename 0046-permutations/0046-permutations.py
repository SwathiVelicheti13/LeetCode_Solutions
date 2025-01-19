class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(nums,ans,visited):
            if len(ans) == len(nums):  # Generate permutations of size 3
                res.append(ans[:])  # Append a copy of the current permutation
                return

            for i in range(len(nums)):
                if not visited[i]:  # If the element is not already used
                    visited[i] = True  # Mark it as used
                    ans.append(nums[i])  # Include it in the current permutation
                    helper(nums, ans, visited)  # Recurse to build further
                    ans.pop()  # Backtrack: Remove the element
                    visited[i] = False  # Unmark the element

        visited = [False] * len(nums)
        helper(nums, [], visited)
        print(res) 
        return res