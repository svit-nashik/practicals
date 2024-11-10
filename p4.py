def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            dp[i][w] = dp[i - 1][w] if weights[i - 1] > w else max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    return dp[n][capacity]

# User input
n = int(input("Number of items: "))
values = [int(input(f"Value of item {i+1}: ")) for i in range(n)]
weights = [int(input(f"Weight of item {i+1}: ")) for i in range(n)]
capacity = int(input("Capacity of knapsack: "))

print("Maximum value:", knapsack(weights, values, capacity))