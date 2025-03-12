from typing import List 
from collections import defaultdict 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(set),defaultdict(set),defaultdict(set)
        r = len(board)
        c = len(board[0])
        for i in range(r):
            for j in range(c):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i//3, j//3)]:
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3,j//3)].add(board[i][j])
        
        return True