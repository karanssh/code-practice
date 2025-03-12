from collections import defaultdict 

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        l = 0
        cnt= defaultdict(int)
        for r in range(len(s)):
            cnt[s[r]]+=1
            while len(cnt)==3:
                # we found a,b,c all three, so now we can do manipulation of our window
                res += (len(s) - r)
                cnt[s[l]]-=1
                if cnt[s[l]] == 0:
                    cnt.pop(s[l])
                l+=1
        
        return res

        