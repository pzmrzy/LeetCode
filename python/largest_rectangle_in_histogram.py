class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = []
        res = 0
        for i in range(len(heights)):
            while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                nind = stack.pop()
                nh = heights[nind]
                sidx = stack[-1] if len(stack) > 0 else -1
                res = max((i - sidx - 1) * nh, res)
            stack.append(i)
        return res
