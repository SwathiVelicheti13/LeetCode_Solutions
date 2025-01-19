from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]:
            return
        
        n, m = len(board), len(board[0])
        q = deque()

        # Add all boundary 'O' cells to the queue
        for i in range(n):
            if board[i][0] == 'O':
                q.append((i, 0))
            if board[i][m - 1] == 'O':
                q.append((i, m - 1))
        for j in range(m):
            if board[0][j] == 'O':
                q.append((0, j))
            if board[n - 1][j] == 'O':
                q.append((n - 1, j))

        # Direction array for moving up, down, left, right
        direc = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        visited = set()  # Keep track of visited cells

        while q:
            r, c = q.popleft()

            # If already visited, continue
            if (r, c) in visited:
                continue
            visited.add((r, c))

            # For every 'O' connected to the border, mark it as visited
            for dr, dc in direc:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 'O':
                    q.append((nr, nc))

        # Now change the board, replace unvisited 'O' with 'X' and visited 'O' (safe) back to 'O'
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'
                elif board[i][j] == 'O' and (i, j) in visited:
                    board[i][j] = 'O'