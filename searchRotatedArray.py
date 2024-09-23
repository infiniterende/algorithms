def search(nums, target):
    left = 0
    right = len(nums) - 1
    pivot = -1

    while left <= right:
        mid = (left+right) // 2
        if nums[mid] <= nums[-1]:
            pivot = mid
            right = mid - 1
        else:
            left = mid + 1

    def binary_search(left, right, target):
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    n = len(nums)
    right_index = binary_search(pivot, n-1, target)
    left_index = binary_search(0, pivot-1, target)
    return right_index if right_index != -1 else left_index
