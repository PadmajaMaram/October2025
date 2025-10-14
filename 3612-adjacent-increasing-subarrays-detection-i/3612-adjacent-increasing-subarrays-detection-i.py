class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n < 2 * k:
            return False
        a= [1] * n  
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                a[i] = a[i + 1] + 1
        for i in range(n - 2 * k + 1):
            if a[i] >= k and a[i + k] >= k:
                return True
        return False


        