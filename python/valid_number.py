import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pat = [r'^[+|-]?\d+$', r'^[+|-]?\d+\.\d*$', r'^[+|-]?\d*\.\d+$', r'^[+|-]?\d+e[+|-]?\d+$', r'^[+|-]?\d+\.\d*e[+|-]?\d+$', r'^[+|-]?\d*\.\d+e[+|-]?\d+$']
        s = s.strip().lower()
    	for p in pat:
    		if re.match(p, s):
    			return True
    	return False
