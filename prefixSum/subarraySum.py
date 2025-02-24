def subarraySum(nums, k):

    res = 0
    currSum = 0
    prefixSums = {0: 1}

    for num in nums:
        currSum += num
        diff = currSum - k
        res += prefixSums.get(diff, 0)
        prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)

    return res
