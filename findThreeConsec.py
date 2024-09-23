class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        left = -num
        right = 2*num
        while left <= right:
            mid = (left+right) // 2
            total = mid + mid-1 + mid + 1
            if total == num:
                return [mid-1, mid, mid+1]
            elif total > num:
                right = mid - 1
            elif total < num:
                left = mid + 1

        return []
