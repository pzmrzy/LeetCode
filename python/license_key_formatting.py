class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '').upper()
        l = len(S)
        t = K if l % K == 0 else l % K
        res = S[:t]
        while t < l:
            res += '-' + S[t: t + K]
            t += K
        return res
