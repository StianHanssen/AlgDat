from sys import stdin

Inf = 1000000000

def minCoinsGreedy(coins, value):
    if value <= 0:
        return 0
    count = 0
    for coin in coins:
        if coin == value:
            return count + 1
        if coin < value:
            count += value // coin
            value %= coin
            if not value:
                break
    return count

def minCoinsDynamic(coins, value):
    if value <= 0:
        return 0
    useful_coins = []
    for coin in coins:
        if coin == value:
            return 1
        elif coin < value:
            useful_coins.append(coin)
    sol_list = [0] * (value + 1)
    for balance in xrange(1, value + 1):
        sol_list[balance] = min([Inf if balance - coin < 0 else 1 + sol_list[balance - coin] for coin in useful_coins])
    return sol_list[value]

def canUseGreedy(coins):
    amounts = []
    for i in xrange(len(coins) - 1):
        if coins[i] % coins[i + 1]:
            quotient = (coins[i] // coins[i + 1]) + 1
            difference = coins[i + 1] * (quotient) - coins[i]
            amounts.append((difference, quotient))
    for amount in amounts:
        i = 0
        count = 0
        while amount[0] > 0:
            if amount[0] < coins[i]:
                i += 1
                continue
            quotient = amount[0] // coins[i]
            amount = (amount[0] - (coins[i] * quotient), amount[1])
            count += quotient
        if count >= amount[1]:
            return False
    return True

def main():
    coins = [int(c) for c in stdin.readline().split()]
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
