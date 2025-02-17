from typing import List


def canBeValid(s: str, locked: str) -> bool:
        lockedStack = []
        unlockedStack = []
        
        for i in range(len(s)):
            if locked[i] == '0':
                unlockedStack.append(i)
            elif s[i] == '(':
                lockedStack.append(i)
            else:
                if lockedStack:
                    lockedStack.pop()
                elif unlockedStack:
                    unlockedStack.pop()
                else:
                    return False
        while lockedStack and unlockedStack and lockedStack[-1]<unlockedStack[-1]:
            lockedStack.pop()
            unlockedStack.pop()
        if lockedStack:
            return False
        
        return True if len(unlockedStack)%2==0 else False


print(canBeValid("()()", "0000"))
print(canBeValid("))()))", "010100"))
