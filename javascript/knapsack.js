function knapsack(weights, values, capacity) {
  n = weights.length;
  let dp = Array(n + 1)
    .fill()
    .map(() => Array(capacity + 1).fill(0));
  for (let i = 0; i < n; i++) {
    for (let w = 0; w < capacity; w++) {
      if (w == 0 || i == 0) {
        dp[i][w] = 0;
      } else if (w <= weights[i]) {
        dp[i][w] = dp[i - 1][w];
      } else {
        dp[i][w] = Math.max(
          dp[i - 1][w],
          values[i - 1] + dp[i - 1][w - weights[i - 1]]
        );
      }
    }
  }
  return dp[n][capacity];
}
