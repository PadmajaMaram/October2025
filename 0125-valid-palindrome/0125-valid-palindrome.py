class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(c.lower() for c in s if c.isalnum())
        low = 0
        high = len(s)-1 
        if not s:
            return True
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True
        