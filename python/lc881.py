from typing import List


def numRescueBoats( people: List[int], limit: int) -> int:
    people.sort()
    l =0 
    r= len(people)-1
    res = 0
    while l<=r: # till we traverse the entire thing
        while people[r] == limit:
            res+=1 # this guy gets his own fucking boat
            r-=1
        if people[l]+people[r] >limit:
            r-=1
            res +=1 # this guy gets his own fucking boat
        elif people[l]+ people[r]<=limit:
            # these guys gotta share
            l +=1
            r-=1
            res+=1

    
    return res



print(numRescueBoats([3,2,2,1],3))