from typing import List

def calPoints(operations: List[str]) -> int:
        s = []
        for o in operations:
            match o:
                case "C":
                    s.pop()
                case "D":
                    s.append(s[-1]*2)
                case "+": s.append(s[-1]+s[-2])
                case _:
                    s.append(int(o))
        return sum(s)

print(calPoints(["5","2","C","D","+"]))