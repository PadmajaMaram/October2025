class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = n
        while True:
            num = i      
            binary = ""  
            while num > 0:
                remainder = num % 2
                binary = str(remainder) + binary
                num = num // 2
            if "0" not in binary:
                return i   
            i += 1
