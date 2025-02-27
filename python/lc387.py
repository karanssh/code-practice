class Solution:
    def firstUniqChar(self, s: str) -> int:
        ocm = {}
        for i in range(len(s)):
            if s[i] not in ocm:
                ocm[s[i]] = set()
            ocm[s[i]].add(i)
        print(ocm)

        for i in range(len(s)):
            if len(ocm[s[i]]) == 1:
                return i

        return -1

if __name__ == "__main__":
    ob = Solution()
    
    print(ob.firstUniqChar("fffa"))