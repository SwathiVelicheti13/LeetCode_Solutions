class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        hashmap = {}
        for num in nums2:
            while stack and stack[-1]<num:
                val = stack.pop()
                hashmap[val] = num
            stack.append(num)

        while len(stack)>0:
            val = stack.pop()
            hashmap[val] = -1

        ngeList = []

        for num in nums1:
            if num in hashmap:
                ngeList.append(hashmap[num])
        return ngeList
        