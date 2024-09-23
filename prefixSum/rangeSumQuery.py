def range_sum_query(nums, i, j):
    prefixSum = []
    curr = 0
    for num in nums:
        curr += num
        prefixSum.append(curr)
    right_sum = prefixSum[j]
    left_sum = prefixSum[i - 1] if i > 0 else 0
    return right_sum - left_sum
