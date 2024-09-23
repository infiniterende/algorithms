function longestIncreasingSequence(array) {
  let dp = Array(array.length).fill(0);
  dp[0] = 0;
  maxLen = 0;

  for (let i = 1; i < array.length; i++) {
    let previousEl = array[i - 1];
    dp[i] = dp[0] + 1;
    for (let j = 1; j < i; j++) {
      let previousJEl = array[j - 1];
      if (previousJEl < previousEl) {
        dp[i] = max(dp[i], dp[j] + 1);
      }
    }
    maxLen = max(maxLen, dp[i]);
  }
  return maxLen;
}
