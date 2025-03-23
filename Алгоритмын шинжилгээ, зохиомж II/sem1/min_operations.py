def min_operations(target, memo=None):
    if memo is None:
        memo = {}
    if target == 0:
        return 0  
    if target == 1:
        return 1  
    if target in memo:
        return memo[target]

    if target % 2 == 0:
        memo[target] = 1 + min_operations(target // 2, memo)
    else:
        memo[target] = 1 + min_operations(target - 1, memo)
    print(memo)
    return memo[target]

results = [min_operations(i) for i in range(0, 10)]
print(results)
