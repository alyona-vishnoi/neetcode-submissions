class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def backtrack(r, c, k):
            # k = index in word we're trying to match
            # fail cases
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if (r, c) in visited:
                return False
            if board[r][c] != word[k]:
                return False

            # success case
            if k == len(word) - 1:
                return True

            # choose
            visited.add((r, c))

            # explore 4 directions
            found = (
                backtrack(r + 1, c, k + 1) or
                backtrack(r - 1, c, k + 1) or
                backtrack(r, c + 1, k + 1) or
                backtrack(r, c - 1, k + 1)
            )

            # un-choose / backtrack
            visited.remove((r, c))

            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False