class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m = len(image)
        if m == 0:
            return 0
        n = len(image[0])
        minx, miny, maxx, maxy = m, n, 0, 0
        for i in range(m):
            for j in range(n):
                if image[i][j] == '1':
                    if i > maxx:
                        maxx = i
                    if i < minx:
                        minx = i
                    if j > maxy:
                        maxy = j
                    if j < miny:
                        miny = j
        print minx, miny, maxx, maxy
        if x > maxx:
            maxx = x
        if x < minx:
            minx = x
        if y > maxy:
            maxy = y
        if y < miny:
            miny = y
        print minx, miny, maxx, maxy
        return (maxx - minx + 1) * (maxy - miny + 1)
