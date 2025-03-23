def max_sum_rob_income(arr, n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n < 0:
        return 0
    
    memo[n] = max(arr[n] + max_sum_rob_income(arr, n - 2, memo), max_sum_rob_income(arr, n - 1, memo))
    return memo[n]

arr1 = [13, 7, 3, 9, 1]
result1 = max_sum_rob_income(arr1, len(arr1) - 1)
print(result1)

arr2 = [8, 12, 15, 20]
result2 = max_sum_rob_income(arr2, len(arr2) - 1)
print(result2)