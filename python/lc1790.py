from collections import defaultdict
from typing import List


def areAlmostEqual(s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        if len(s1)!=len(s2):
            return False
        s1m = defaultdict(int)
        s2m = defaultdict(int)
        for i in range(len(s1)):
            s1m[s1[i]] += 1
        for j in range(len(s2)):
            s2m[s2[j]] += 1
        if s1m!=s2m:
             return False
        allowedDiff = 0
        for i in range(len(s1)):
            # position of char in both strings is same
            if s1[i] != s2[i]:
                allowedDiff+=1
        
        if allowedDiff!=2:
            return False
        
        return True


print(areAlmostEqual("akrjnhuojtkhlqdfifwxbsmphhcchuqcconcvplcyxjpi", "akrjnhuojtkhlxdfifwqbsmphhcchuqcconcvplcyxjpi"))