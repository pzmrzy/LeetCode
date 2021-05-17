class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = False
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + 1 > 9:
                digits[i] = 0
                carry = True
            else:
                digits[i] = digits[i] + 1
                carry = False
                break
        if carry:
            return [1] + digits 
        else:
            return digits

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        digits[0] += 1
        ex = 0
        for i in range(len(digits)):
            t = digits[i] + exp
            digits[i] = t % 10
            ex = t / 10
        
        if (ex == 1):
            digits.append(1)
        digits.reverse()
        return digits
