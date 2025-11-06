def knapsack_dp():
    n = int(input("Enter number of items: "))
    wt, val = [], []

    for i in range(n):
        w, v = map(int, input(f"Item {i+1} (weight value): ").split())
        wt.append(w)
        val.append(v)

    W = int(input("Enter knapsack capacity: "))

    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w - wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    print("\nMaximum Profit:", dp[n][W])

knapsack_dp()
