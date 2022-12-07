def isIsomorphic(s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

if __name__ == "__main__":
    print(isIsomorphic("egg", "add"))
    print(isIsomorphic("flight", "flow"))
