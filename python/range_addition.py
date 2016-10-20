class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        result = [0] * length 
        
        for begin, end, val in updates:
            result[begin] = result[begin] + val
            if end + 1 < length:
                result[end + 1] = result[end + 1] - val

        for i in range(1, length):
            result[i] += result[i - 1]
        
        return result
