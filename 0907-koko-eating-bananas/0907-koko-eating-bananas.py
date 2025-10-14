from math import ceil

class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        ans = high  
        while low <= high:
            mid = (low + high) // 2
            total = sum(ceil(num / float(mid)) for num in piles)  
            if total <= h:
                ans = mid        
                high = mid - 1  
            else:
                low = mid + 1
        return ans
