class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                if (
                    ("row", r, num) in seen or
                    ("col", c, num) in seen or
                    ("box", r // 3, c // 3, num) in seen
                ):
                    return False

                seen.add(("row", r, num))
                seen.add(("col", c, num))
                seen.add(("box", r // 3, c // 3, num))

        return True