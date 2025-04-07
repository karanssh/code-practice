from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s= []
        res = [0]* len(temperatures)
        for i, t in enumerate(temperatures):
            if not s:
                s.append((t,i))
            else:
                while s and s[-1][0]<t:
                    temp, idx = s.pop()
                    res[idx] = i-idx
                s.append((t,i))
        return res
    def dailyTemperatures2(self, temperatures: List[int]) -> List[int]:
        s= []
        res = [0]* len(temperatures)
        for i, t in enumerate(temperatures):
            while s and t>s[-1][0]:
                _, idx = s.pop()
                res[idx] = i -idx
            s.append([t,i])


        return res
