from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowLength = len(s1)
        if windowLength > len(s2): 
            return False
        
        s1c = Counter(s1)
        s2c = {}
        l = 0
        
        for r in range(len(s2)):
            # Add the current character to the window
            if s2[r] not in s2c:
                s2c[s2[r]] = 0
            s2c[s2[r]] += 1
            
            # Shrink the window if it exceeds the desired size
            if (r - l + 1) > windowLength:
                s2c[s2[l]] -= 1
                if s2c[s2[l]] == 0:
                    s2c.pop(s2[l])
                l += 1
            
            # Check if the current window matches the target
            if (r - l + 1) == windowLength and s1c == s2c:
                return True
        
        return False

if __name__ == "__main__":
    obj = Solution()
    print(obj.checkInclusion("adc", "dcda"))  # Output: True
    print(obj.checkInclusion("ab", "eidboaoo"))  # Output: False