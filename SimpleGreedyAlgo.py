def coin_change_greedy(amount, coins):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

amount = 57
coins = [25, 10, 5, 1]
change = coin_change_greedy(amount, coins)
print("Coins used:", change)

#Output = Coins used: [25, 25, 5, 1, 1]
