class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        l = len(guess)
        S = [0 for i in range(10)]
        G = [0 for i in range(10)]
        A = 0
        B = 0
        for i in range(l):
            if (secret[i] == guess[i]):
                A += 1
            S[int(secret[i])] += 1
            G[int(guess[i])] += 1
        for i in range(10):
            B += max(S[i], G[i]) - abs(S[i] - G[i])
        B -= A
        result = '%dA%dB' % (A, B)
        return result
