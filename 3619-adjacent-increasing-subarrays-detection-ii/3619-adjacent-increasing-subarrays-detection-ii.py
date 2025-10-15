class Solution(object):
    def maxIncreasingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <=2:
            return 1
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                left[i] = left[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right[i] = right[i + 1] + 1
        ans = 0
        for i in range(n - 2):
            ans = max(ans, min(left[i], right[i + 1]))
        return ans
