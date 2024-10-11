def fibonacci(n):
    # Create a DP table to store Fibonacci values
    dp = [0] * (n + 1)
    dp[1] = 1  # Base case

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # Fill the table using previous values

    return dp[n]

# Example usage
print(fibonacci(10))  # Output: 55
