class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        l = len(gas)
        res = summ = tot = 0
        for i in range(l):
            summ += gas[i] - cost[i]
            if summ < 0:
                tot += summ
                summ, res = 0, i + 1
        tot += summ
        return -1 if tot < 0 else res
