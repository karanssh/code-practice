from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res= []
        stack = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN<n:
                stack.append("(")
                backtrack(openN+1, closeN)
                stack.pop()
            if closeN<openN:
                stack.append(")")
                backtrack(openN, closeN+1)
                stack.pop()
        
        backtrack(0,0)
        return res
    
    def generateParenthesis2(self, n: int) -> List[str]:

        res = []

        def backtrack(open_n, closed_n, path):
            if open_n == closed_n == n:
                res.append(path)
                return
            if open_n < n:
                backtrack(open_n + 1, closed_n, path + "(")

            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path + ")")
                
            backtrack(0, 0, "")

        return res