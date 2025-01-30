class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        direction = 0  # 0: North, 1: East, 2: South, 3: West
        
        # Direction vectors for movement
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for instruction in instructions:
            if instruction == 'G':
                # Move in the current direction
                x += move[direction][0]
                y += move[direction][1]
            elif instruction == 'L':
                # Turn left (counterclockwise)
                direction = (direction - 1) % 4
            elif instruction == 'R':
                # Turn right (clockwise)
                direction = (direction + 1) % 4
        
        # Check if the robot is back at the origin or not facing north
        return (x == 0 and y == 0) or (direction != 0)