class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return  int(format(n, 'b').zfill(32)[::-1], 2)
