class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        ind = 0
        for i in range(len(s)):
            if s[i] == " ":
                s[ind: i] = reversed(s[ind: i])
                ind = i + 1
        s[ind:] = reversed(s[ind: ])
        s.reverse()
