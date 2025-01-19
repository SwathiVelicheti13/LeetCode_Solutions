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

        # Mark all boundary-connected 'O' cells as safe
        while q:
            r, c = q.popleft()
            if 0 <= r < n and 0 <= c < m and board[r][c] == 'O':
                board[r][c] = 'S'  # Mark as safe
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    q.append((r + dr, c + dc))

        # Replace all 'O' with 'X' and 'S' back to 'O'
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'



        

        