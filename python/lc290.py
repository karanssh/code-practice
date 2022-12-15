def wordPattern(pattern: str, s: str) -> bool:
    mp = {}
    sp = {}
    sA = s.split(" ")
    if len(sA) != len(pattern):
        return False
    for i in range(len(pattern)):
        if pattern[i] in mp:
            if mp[pattern[i]] != sA[i]:
                return False
        else:
            mp[pattern[i]] = sA[i]
    return len(mp.values()) == len(set(mp.values()))


if __name__ == "__main__":
    print(wordPattern("abba", "dog cat cat dog"))
    print(wordPattern("abba", "dog cat cat f"))