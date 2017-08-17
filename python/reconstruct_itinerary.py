from Queue import PriorityQueue
from collections import defaultdict

class Solution(object):
    def dfs(self, depar):
        arriv = self.flights[depar]
        while arriv.qsize() > 0:
            tmp = arriv.get()
            self.dfs(tmp)
        self.path.append(depar)

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.path = []
        self.flights = defaultdict(lambda: PriorityQueue())
        for ticket in tickets:
            self.flights[ticket[0]].put(ticket[1])
        self.dfs("JFK")
        return self.path[::-1]
