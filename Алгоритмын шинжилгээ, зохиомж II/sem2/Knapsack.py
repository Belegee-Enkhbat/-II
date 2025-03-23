def knapsack(prices, weights, capacity):
    n = len(prices)
    dp = [0] * (capacity + 1)
    print(dp)
    selected_items = [[] for _ in range(capacity + 1)]

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            new_value = dp[w - weights[i]] + prices[i]
            if new_value > dp[w]:
                dp[w] = new_value
                selected_items[w] = selected_items[w - weights[i]] + [(weights[i], prices[i])]
    return dp[capacity]


prices = [1, 6, 18, 22, 28]
weights = [1, 2, 5, 6, 7]
capacity = 11

print("Hariu", knapsack(prices, weights, capacity))


prices1 = [19,19,13,13,13]
weights1 = [7,5,4,2,3]
capacity1 = 11
print("Hariu1", knapsack(prices1, weights1, capacity1))


prices2 = [19,19,13,13,13]
weights2 = [7,5,4,2,3]
capacity2 =12
print("Hariu2", knapsack(prices2, weights2, capacity2))

