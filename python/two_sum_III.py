class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.dic = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.dic.setdefault(number, 0)
        self.dic[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for key in self.dic:
            t = value - key
            if t != key:
                if t in self.dic:
                    return True
            else:
                if self.dic[t] > 1:
                    return True
        return False

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
