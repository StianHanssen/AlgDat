from sys import stdin

def minCoinsGreedy(coins, value):
    count = 0
    for coin in coins:
        if coin <= value:
            count += value // coin
            value %= coin
            if not value:
                break
    return count

def minCoinsDynamic(coins, value):
    useful_coins = []
    for coin in coins:
        if coin == value:
            return 1
        elif coin < value:
            useful_coins.insert(0, coin)
    useful_coins = useful_coins[1:]
    solution_matrix = [[x for x in xrange(value + 1)]]
    for i in xrange(len(useful_coins)):
        coin = useful_coins[i]
        solution_matrix.append(solution_matrix[i][:coin])
        for j in xrange(coin, value + 1):
            solution_matrix[i + 1].append(min(solution_matrix[i][j], 1 + solution_matrix[i + 1][j - coin]))
    return solution_matrix[-1][-1]

def canUseGreedy(coins):
    for i in xrange(len(coins) - 1):
        if coins[i] % coins[i + 1] != 0:
            return False
    return True

def main():
    Inf = 1000000000
    coins = []
    for c in stdin.readline().split():
        coins.append(int(c))
    coins.sort()
    coins.reverse()
    method = stdin.readline().strip()
    if method == "graadig" or (method == "velg" and canUseGreedy(coins)):
        for line in stdin:
            print minCoinsGreedy(coins, int(line))
    else:
        for line in stdin:
            print minCoinsDynamic(coins, int(line))

main()
#test = [203, 100, 18, 16, 7, 5, 3, 1]
#print minCoinsDynamic(test, 86)
