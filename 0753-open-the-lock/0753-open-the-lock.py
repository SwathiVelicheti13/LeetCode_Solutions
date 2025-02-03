from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        
        # If the target is a deadend or the start itself is a deadend, return -1
        if '0000' in dead or target in dead:
            return -1
        
        # Initialize BFS queue
        queue = deque([('0000', 0)])  # (current state, number of moves)
        visited = set('0000')  # Set of visited states
        
        # Possible moves for each digit (up or down by 1, wrapping around)
        directions = [1, -1]
        
        while queue:
            state, steps = queue.popleft()
            
            # If we've reached the target, return the number of moves
            if state == target:
                return steps
            
            # Generate next possible states by rotating each digit
            for i in range(4):  # There are 4 digits
                for direction in directions:  # For each direction (+1 or -1)
                    new_digit = (int(state[i]) + direction) % 10  # Wraps around using modulo
                    new_state = state[:i] + str(new_digit) + state[i+1:]
                    
                    # If the new state is not visited and not a deadend, add it to the queue
                    if new_state not in visited and new_state not in dead:
                        visited.add(new_state)
                        queue.append((new_state, steps + 1))
        
        # If no solution is found, return -1
        return -1

        
        