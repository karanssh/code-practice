from typing import List 


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        sc, pc = {}, {}
        for i in range(len(p)):
            pc[p[i]] = pc.get(p[i], 0) + 1
            sc[s[i]] = sc.get(s[i], 0) + 1
        
        res = [0] if pc == sc else []
        l = 0

        for r in range(len(p), len(s)):
            

            sc[s[r]] = sc.get(s[r], 0) + 1
            sc[s[l]] = sc[s[l]]-1

            if sc[s[l]] == 0:
                sc.pop(s[l])
            l+=1
            if sc == pc:
                res.append(l)
            
        return res
    
if __name__ == "__main__":
    
    obj = Solution()
    print(obj.findAnagrams("cbaebabacd", "abc"))
