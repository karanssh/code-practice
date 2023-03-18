def hasAllCodes(s: str, k: int) -> bool:
        se = set()
        windowStart = 0
        for windowEnd in range(len(s)):
            if windowEnd - windowStart +1 == k:
                se.add(s[windowStart:windowEnd+1])
                windowStart +=k
        
        if len(se) != 2**k:
            return False
        return True


print(
    hasAllCodes("00110110",2),
    hasAllCodes("0110",1)
)