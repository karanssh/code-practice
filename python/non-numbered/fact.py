# from DP recursive practice book


def factRecursion(n: int) -> int:
    if n<=1:
        return 1
    return n * factRecursion(n-1)



def run():
    print(factRecursion(5))

run()