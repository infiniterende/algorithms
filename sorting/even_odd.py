def even_odd(nums):
    i = 0
    j = len(nums) - 1

    while i <= j:
        if nums[i] % 2 == 0:
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1

    return nums
