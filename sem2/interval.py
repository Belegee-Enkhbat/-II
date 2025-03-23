def binary_search(jobs, index):
    low, high = 0, index - 1
    while low <= high:
        mid = (low + high) // 2
        if jobs[mid][1] <= jobs[index][0]:
            if mid + 1 < index and jobs[mid + 1][1] <= jobs[index][0]:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1
    return -1


def weighted_interval_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])
    n = len(jobs)
    dp, selected_jobs = [0] * (n + 1), [[] for _ in range(n + 1)]
    p = [binary_search(jobs, i) for i in range(n)]

    for i in range(1, n + 1):
        include_profit = jobs[i - 1][2] + (dp[p[i - 1] + 1] if p[i - 1] != -1 else 0)
        if dp[i - 1] > include_profit:
            dp[i], selected_jobs[i] = dp[i - 1], selected_jobs[i - 1]
        else:
            dp[i], selected_jobs[i] = include_profit, selected_jobs[p[i - 1] + 1] + [jobs[i - 1]]

    print(selected_jobs[n])
    return dp[n]

jobs2 = [(1, 3, 5), (2, 5, 6), (4, 6, 5), (6, 7, 4), (5, 8, 11), (7, 9, 2), (8, 11, 10), (9, 12, 1)]


test1 = [(3, 9, 60,1), (8, 9, 10,2), (6, 8, 20,3), (0, 6, 70,4),(6,9,40,5),(3,5,30,6),(1,4,40,7),(1,3,30,8)]
test2 = [(5,8,4000,1),(1,4,6000,2),(3,4,1800,3),(6,8,5000,4),(3,5,2000,5),(4,8,6000,6),(2,4,2000,7),(0,3,5000,8),(0,8,4500,9)]

print("Hariu:", weighted_interval_scheduling(jobs2))


print("Hariu test1:", weighted_interval_scheduling(test1))
print("Hariu test2:", weighted_interval_scheduling(test2))