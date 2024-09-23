function fibonacci(n) {
  let nums = [0, 1];
  for (let i = 2; (i += 1); i < n + 1) {
    nums.push(nums[i - 1] + nums[i - 2]);
  }
  return nums[n];
}
