def unbounded_knapsack_recursive(C, w, p, n):
    if C == 0:
        return 0
    
    max_profit = 0
    for i in range(n):
        if w[i] <= C:
            max_profit = max(max_profit, p[i] + unbounded_knapsack_recursive(C - w[i], w, p, n))
    
    return max_profit


def unbounded_knapsack_bottom_up(C, w, p, n):
    dp = [0] * (C + 1)
    
    for c in range(1, C + 1):
        for i in range(n):
            if w[i] <= c:
                dp[c] = max(dp[c], p[i] + dp[c - w[i]])
    
    return dp[C], dp


if __name__ == "__main__":
    print("=" * 50)
    print("Test Case 1: C=14, w=[4,6,8], p=[7,6,9]")
    print("=" * 50)
    C = 14
    w = [4, 6, 8]
    p = [7, 6, 9]
    n = len(w)
    
    result, dp = unbounded_knapsack_bottom_up(C, w, p, n)
    print(f"dp array: {dp}")
    print(f"P(14) = {result}")
    
    print("\n" + "=" * 50)
    print("Test Case 2: C=14, w=[5,6,8], p=[7,6,9]")
    print("=" * 50)
    w2 = [5, 6, 8]
    p2 = [7, 6, 9]
    n2 = len(w2)
    
    result2, dp2 = unbounded_knapsack_bottom_up(C, w2, p2, n2)
    print(f"dp array: {dp2}")
    print(f"P(14) = {result2}")
    
    print("\n" + "=" * 50)
    print("Recursive Results (for verification)")
    print("=" * 50)
    print(f"Test 1 recursive: P(14) = {unbounded_knapsack_recursive(14, w, p, n)}")
    print(f"Test 2 recursive: P(14) = {unbounded_knapsack_recursive(14, w2, p2, n2)}")