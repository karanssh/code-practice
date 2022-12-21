def removeDuplicates(s: str, k: int) -> str:
    
    st = []
    for i in range(len(s)):
        if len(st)>=k:
            # do something
            needsPop = True
            curChar = st[-1]
            for j in range(k):
                if st[len(st)-j-1] != curChar:
                    needsPop = False
            if needsPop:
                for _ in range(k):
                    st.pop()

        st.append(s[i])

    return "".join(st) if st else ""

def removeDuplicates2(s: str, k: int) -> str:
        distinct = set(s)
        toRemove = list()
        for char in distinct:
            toRemove.append(char*k)
        
        while True:
            start = s
            for dup in toRemove:
                if dup in s:
                    s = s.replace(dup, "")
            if start == s:
                return s

removeDuplicates2("pbbcggttciiippooaais", 2)