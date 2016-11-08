import time
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if len(seqs) == 0:
            return False
        edge = {}
        inbound = {}
        for o in org:
            edge[o] = []
            inbound[o] = 0

        for s in seqs:
            if len(s) == 1:
                if s[0] not in edge:
                    return False
            for i in range(1, len(s)):
                try:
                    edge[s[i - 1]].append(s[i])
                    inbound[s[i]] += 1
                except:
                    return False

        for n in org:
            n1 = 0
            if inbound[n] == 0:
                for v in edge[n]:
                    inbound[v] -= 1
                    if inbound[v] == 0:
                        n1 += 1
                if n1 != 1 and n != org[-1]:
                    return False
                inbound[n] = -1
            else:
                return False
        return True
