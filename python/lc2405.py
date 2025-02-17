def partitionString(s: str) -> int:
        res = 0
        seen = {}
        for i in range(len(s)):
            if s[i] in seen:
                res+=1
                seen = {}
            seen[s[i]] = True
        if len(seen)>0:
            res+=1
        return res


if __name__ == "__main__":
    
    
    print(partitionString("abacaba"))