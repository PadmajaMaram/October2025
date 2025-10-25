class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        result=""
        while columnNumber>0:
            columnNumber-=1
            rem=columnNumber%26
            let=chr(65+rem)
            result=let+result
            columnNumber//=26
        return result



        