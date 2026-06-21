class Solution:
    def maxDistance(self, moves: str) -> int:
        U = moves.count('U')
        D = moves.count('D')
        L = moves.count('L')
        R = moves.count('R')
        x = moves.count('_')
        y = R - L
        z = U - D
        return abs(y) + abs(z) + x
