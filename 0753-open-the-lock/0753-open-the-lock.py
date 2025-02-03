from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        if '0000' in dead or target in dead:
            return -1

        q = deque([('0000',0)])

        visited = set()

        while q:
            state, steps = q.popleft()

            if state == target:
                return steps

            
            for i in range(4):
                direc = [-1,1]

                for dire in direc:
                    new_digit = (int(state[i]) + dire)%10
                    new_state = state[:i]+str(new_digit)+state[i+1:]

                    if new_state not in visited and new_state not in dead:
                        visited.add(new_state)
                        q.append((new_state,steps+1))
        return -1
        

        
        