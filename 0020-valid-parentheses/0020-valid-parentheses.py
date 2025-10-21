class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in map:  
                if not stack or stack.pop() != map[ch]:
                    return False
            else:  
                stack.append(ch)

        return not stack
