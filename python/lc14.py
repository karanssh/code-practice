from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        def computePrefix(a: str, b: str) -> str:
            pr = ""
            if len(a)<len(b):
                # swap the pairs to make a biggest
                a, b = b, a
            for i in range(len(b)):
                if a[i]==b[i]:
                    pr+= b[i]
                else:
                    break
            return pr

        curPrefix = strs[0]
        for i in range(1, len(strs)):
            if curPrefix == "":
                return ""
            curPrefix = computePrefix(curPrefix, strs[i])
        return curPrefix


if __name__ == "__main__":
    print(longestCommonPrefix(["flight", "flow"]))
    print(longestCommonPrefix(["dog","racecar","car"]))
    print(longestCommonPrefix(["flower","flow","flight"]))

    

    