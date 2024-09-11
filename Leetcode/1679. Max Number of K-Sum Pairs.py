class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right, operation = 0, len(nums) - 1 , 0

        while left < right:
            if ((nums[left] + nums[right]) == k):
                left += 1
                right -= 1
                operation += 1
            elif ((nums[left] + nums[right]) < k):
                left += 1
            else:
                right -= 1
        return operation