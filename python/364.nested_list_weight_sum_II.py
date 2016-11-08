# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def dfs(self, nest, d):
        for l in nest.getList():
            if l.isInteger():
                self.depth.setdefault(d, [])
                self.depth[d].append(l.getInteger())
            else:
                self.dfs(l, d + 1)
    
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if nestedList == []:
            return 0
            
        self.depth = {}
        for l in nestedList:
            if l.isInteger():
                self.depth.setdefault(0, [])
                self.depth[0].append(l.getInteger())
            else:
                self.dfs(l, 1)
                
        maxd = max(self.depth.keys()+[0]) + 1
        res = 0
        for key in self.depth:
            res += (maxd - key) * sum(self.depth[key])
        return res    
        
