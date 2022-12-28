def numSquares( n: int) -> int:

    sq = []
    for i in range(1,n+1):
        sq.append(i*i)
        if i*i >= n:
            break
    print(sq)

    print(bestSum(n, sq, {}))
    return len(bestSum(n, sq, {}))

def bestSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    shortestCombination = None
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers, memo)

        if remainderCombination is not None:
            combination = remainderCombination + [num]
            if shortestCombination is None or len(combination) < len(shortestCombination):
                shortestCombination = combination.copy()

    # print(str(targetSum) + "---------" + str(shortestCombination))
    if shortestCombination:
        memo[targetSum] = shortestCombination.copy()
    else:
        memo[targetSum] = None
    return shortestCombination

# print(numSquares(12))
print(numSquares(1))