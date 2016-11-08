class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        if len(vec2d) == 1:
            self.vec = vec2d[0]
        elif len(vec2d) == 0:
            self.vec = []
        else:
            self.vec = reduce(lambda x, y: x + y, vec2d)

    def next(self):
        """
        :rtype: int
        """
        t = self.vec[0]
        del self.vec[0]
        return t

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.vec) > 0

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
