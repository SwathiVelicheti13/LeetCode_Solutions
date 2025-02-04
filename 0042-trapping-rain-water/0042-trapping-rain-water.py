class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = 0 
        rightmax = 0
        left_ptr = 0
        right_ptr = len(height)-1
        trapped_water = 0
        while left_ptr<=right_ptr:
            # compare heights at left and right pointers
            if height[left_ptr]<=height[right_ptr]:
                #checking and updating max left bar
                if height[left_ptr]>=leftmax:
                    leftmax = height[left_ptr]
                else:
                    trapped_water+=(leftmax-height[left_ptr])
                left_ptr+=1
            else:
                if height[right_ptr]>=rightmax:
                    rightmax = height[right_ptr]
                else:
                    trapped_water+=(rightmax-height[right_ptr])
                right_ptr= right_ptr-1
        return trapped_water



        