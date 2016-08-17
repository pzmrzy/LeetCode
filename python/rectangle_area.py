class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        x = max((C - A) + (G - E) - (max(C, G) - min(A, E)), 0)
        y = max((D - B) + (H - F) - (max(D, H) - min(B, F)), 0)
        return (C - A) * (D - B) + (G - E) * (H - F) - x * y
