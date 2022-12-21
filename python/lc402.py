from collections import deque 

def removeKdigits(num: str, k: int) -> str:
    l = len(num)
    if k == l:
        return "0"
    s = []
    res = deque()
    i = 0
    while i<l:
        while k>0 and len(s)>0 and s[-1]>num[i]:
            s.pop()
            k-=1
        s.append(num[i])
        i+=1
    
    while k>0:
        s.pop()
        k-=1
    
    while s:
        res.append(s.pop())
    res.reverse()

    while len(res)>1 and res[0] == '0':
        res.popleft()
    return "".join(res)


removeKdigits("10200", 1)

removeKdigits("1432219", 3)

