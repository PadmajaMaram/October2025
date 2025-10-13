class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n = len(letters)
        low, high = 0, n - 1
        ans = letters[0]  # wrap around case

        while low <= high:
            mid = (low + high) // 2
            if letters[mid] > target:
                ans = letters[mid]  # candidate for next greatest
                high = mid - 1
            else:
                low = mid + 1

        return ans
