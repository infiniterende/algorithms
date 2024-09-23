class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # three subarrays - 0, 1, 2
        # [0,1,0,2]
        i = 0
        curr = 0
        k = len(nums) - 1

        while curr <= k:
            if nums[curr] == 0:
                nums[i], nums[curr] = nums[curr], nums[i]
                i += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[k] = nums[k], nums[curr]
                k -= 1
            else:
                curr += 1
