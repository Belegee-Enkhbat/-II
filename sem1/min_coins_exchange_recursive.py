import json  

def min_coins_exchange_recursive(coins, money, memo=None):
    if memo is None:
        memo = {}
    if money == 0:
        return 0  
    if money < 0:
        return float('inf')  

    if money in memo:
        return memo[money]  

    min_count = float('inf')

    for coin in coins:
        res = min_coins_exchange_recursive(coins, money - coin, memo)  
        if res != float('inf'):
            min_count = min(min_count, res + 1)  

    memo[money] = min_count if min_count != float('inf') else -1  

    return memo[money]  


coins = [1, 15, 25]
money = 30
memo_table = {}  

result = min_coins_exchange_recursive(coins, money, memo_table)  
print(result)


# with open('memoization_table.json', 'w') as f:
#     json.dump(memo_table, f, indent=4)

# print(json.dumps(memo_table, indent=4))
