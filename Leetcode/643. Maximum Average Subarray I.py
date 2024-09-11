class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)

        window = sum(nums[:k])
        max_avg = window / k

        for i in range(k, n):
            window += nums[i] - nums[i -k]
            if ((window / k) > max_avg):
                max_avg = window / k
        return max_avg