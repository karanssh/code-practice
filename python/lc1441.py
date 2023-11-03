from typing import List

def buildArray(target: List[int], n: int) -> List[str]:
        res = []
        push = "Push"
        pop = "Pop"
        i = 1
        ct = 0
        while i<=n:
            if ct == len(target):
                break
            
            if i==target[ct]:
                res.append(push)
                ct+=1
            else:
                res.append(push)
                res.append(pop)
                 

            i+=1

        return res

print(buildArray([1,2,3,5], 9))
print(buildArray([1,3], 9))
print(buildArray([1,2,3], 9))