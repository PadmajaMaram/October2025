class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        def findNSE(heights):
            n = len(heights)
            ans = [0] * n
            stack = []
            for i in range(n - 1, -1, -1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if not stack:
                    ans[i] = n
                else:
                    ans[i] = stack[-1]
                stack.append(i)
            return ans
        def findPSE(heights):
            n = len(heights)
            ans = [0] * n
            stack = []
            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if not stack:
                    ans[i] = -1
                else:
                    ans[i] = stack[-1]
                stack.append(i)
            return ans
        n = len(heights)
        nse = findNSE(heights)
        pse = findPSE(heights)
        max_area = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)
        return max_area

        