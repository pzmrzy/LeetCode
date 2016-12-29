import sys
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        if len(rectangles) == 0:
            return False
        if len(rectangles[0]) == 0:
            return False
        area = 0
        x1, y1, x2, y2 = sys.maxint, sys.maxint, -sys.maxint, -sys.maxint
        s = set()
        for tx1, ty1, tx2, ty2 in rectangles:
            x1 = min(x1, tx1)
            x2 = max(x2, tx2)
            y1 = min(y1, ty1)
            y2 = max(y2, ty2)
            area += (tx2 - tx1) * (ty2 - ty1)
            s.remove((tx1, ty1)) if (tx1, ty1) in s else s.add((tx1, ty1)) 
            s.remove((tx1, ty2)) if (tx1, ty2) in s else s.add((tx1, ty2)) 
            s.remove((tx2, ty1)) if (tx2, ty1) in s else s.add((tx2, ty1)) 
            s.remove((tx2, ty2)) if (tx2, ty2) in s else s.add((tx2, ty2)) 
        return len(s) == 4 and (x1, y1) in s and (x1, y2) in s and (x2, y1) in s and (x2, y2) in s and area == (x2 - x1) * (y2 - y1)
