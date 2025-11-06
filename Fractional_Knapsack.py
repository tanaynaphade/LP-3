def fractional_knapsack():
    n = int(input("Enter number of items: "))
    items = []

    for i in range(n):
        w, v = map(float, input(f"Item {i+1} (weight value): ").split())
        items.append((w, v))

    cap = float(input("Enter knapsack capacity: "))
    items.sort(key=lambda x: x[1]/x[0], reverse=True)

    total = 0
    for w, v in items:
        if cap == 0:
            break
        if w <= cap:
            total += v
            cap -= w
        else:
            total += v * (cap / w)
            cap = 0

    print(f"\nMaximum value = {total:.2f}")

fractional_knapsack()
