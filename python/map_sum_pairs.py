class TrieNode(object):
    
    def __init__(self):
        self.count = 0
        self.children = {}

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.dic = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        cur = self.root
        delta = val - self.dic.get(key, 0)
        self.dic[key] = val
        cur.count += delta
        for c in key:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.count += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.count


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
