class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}
        self.lis = []
        self.cap = capacity
        self.use = 0

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.dic:
            self.lis.remove(key)
            self.lis.append(key)
            return self.dic[key]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.get(key) == -1:
            if self.use < self.cap:
                self.dic[key] = value
                self.lis.append(key)
                self.use += 1
            else:
                dk = self.lis.pop(0)
                del self.dic[dk]
                self.lis.append(key)
                self.dic[key] = value
        else:
            self.dic[key] = value
