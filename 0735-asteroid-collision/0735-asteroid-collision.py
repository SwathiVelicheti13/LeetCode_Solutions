class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for a in asteroids:
            while stack and a<0<stack[-1]:
                if -a > stack[-1]:
                    stack.pop()
                    continue
                elif -a == stack[-1]:
                    stack.pop()
                break

            else:
                stack.append(a)
        return stack


        # stack = []

        # for i in range(len(asteroids)):
        #     if asteroids[i]>0:
        #         stack.append(asteroids[i])
        #     else:
        #         while stack and stack[-1]>0 and asteroids[i]< 0 and abs(asteroids[i])>stack[-1]:
        #             stack.pop()
        #     if stack and abs(asteroids[i])== stack[-1]:
        #             stack.pop()
        #     elif len(stack) == 0 or stack[-1]<0:
        #         stack.append(asteroids[i])
        # if stack:
        #     return stack
        # return []
        