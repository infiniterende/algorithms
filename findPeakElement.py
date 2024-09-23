def findPeakElement(nums):
    left = 0
    right = len(nums) - 1
    index = -1

    while left <= right:
        mid = (left+right) // 2
        if mid < len(nums) - 1 and nums[mid] <= nums[mid+1]:
            left = mid + 1
        else:
            index = mid
            right = mid - 1
    return index
