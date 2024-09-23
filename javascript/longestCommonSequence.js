function longestCommonSequence(word1, word2) {
  let n = word1.length;
  let m = word2.length;
  let dp = Array(n + 1)
    .fill()
    .map(() => Array(m + 1).fill(0));
  for (let i = 0; i < n + 1; i++) {
    for (let j = 0; j < m + 1; j++) {
      if (i == 0 || j == 0) {
        dp[i][j] = 0;
      } else if (word1[i - 1] == word2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
      } else {
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }
  return dp[n][m];
}
