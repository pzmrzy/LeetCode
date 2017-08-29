class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        code = re.sub(r'<!\[CDATA\[.*?\]\]>|t', '-', code)
        tmp = None
        while code != tmp:
            tmp = code
            code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
        return code == 't'
