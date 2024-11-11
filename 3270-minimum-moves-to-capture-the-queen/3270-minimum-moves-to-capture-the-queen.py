class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if a == e:
            # Check if the bishop blocks the rook
            if a == c and (d - b) * (d - f) < 0:
                return 2  # Two moves needed as the bishop is in between
            else:
                return 1  # Direct capture possible in one move
        # Check if rook and queen are in the same column
        elif b == f:
            if b == d and (c - a) * (c - e) < 0:
                return 2  # Two moves if the bishop blocks the rook
            else:
                return 1  # Direct capture possible in one move
        # Check if the queen and bishop are on the same \ diagonal
        elif c - e == d - f:
            if a - e == b - f and (a - c) * (a - e) < 0:
                return 2  # Two moves required due to blocking bishop
            else:
                return 1  # Direct capture possible in one move
        # Check if the queen and bishop are on the same / diagonal
        elif c - e == f - d:
            if a - e == f - b and (a - c) * (a - e) < 0:
                return 2
            else:
                return 1
        return 2