from typing import List


def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
    prefixCount = [0] *(len(words)+1)
    vowelSet = {"a", "e", "i", "o", "u"}

    for k, v in enumerate(words):
        temp=0
        if v[0] in vowelSet and v[-1] in vowelSet:
            temp = 1
        prefixCount[k+1] = prefixCount[k] + temp

    res = [0] *len(queries)
    for k,v in enumerate(queries):
        l, r = v[0], v[1]
        res[k] = prefixCount[r+1] - prefixCount[l]
    
    return res

if __name__ == "__main__":
    merge(["a","e","i"],[[0,2],[0,1],[2,2]])