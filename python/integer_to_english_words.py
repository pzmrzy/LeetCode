class Solution(object):
    def lessthan20(self, n):
        if n == 0:
            return ""
        if n == 1:
            return "One"
        if n == 2:
            return "Two"
        if n == 3:
            return "Three"
        if n == 4:
            return "Four"
        if n == 5:
            return "Five"
        if n == 6:
            return "Six"
        if n == 7:
            return "Seven"
        if n == 8:
            return "Eight"
        if n == 9:
            return "Nine"
        if n == 10:
            return "Ten"
        if n == 11:
            return "Eleven"
        if n == 12:
            return "Twelve"
        if n == 13:
            return "Thirteen"
        if n == 14:
            return "Fourteen"
        if n == 15:
            return "Fifteen"
        if n == 16:
            return "Sixteen"
        if n == 17:
            return "Seventeen"
        if n == 18:
            return "Eighteen"
        if n == 19:
            return "Nineteen"
    def toword(self, n):
        pre = ""
        if n >= 100:
            pre = self.lessthan20(n/100) + " Hundred "
        nn = n % 100
        if nn < 20:
            return pre + self.lessthan20(nn)
        if nn < 30:
            return pre + "Twenty " + self.lessthan20(n%10)    
        if nn < 40:
            return pre + "Thirty " + self.lessthan20(n%10)
        if nn < 50:
            return pre + "Forty " + self.lessthan20(n%10)
        if nn < 60:
            return pre + "Fifty " + self.lessthan20(n%10)
        if nn < 70:
            return pre + "Sixty " + self.lessthan20(n%10)
        if nn < 80:
            return pre + "Seventy " + self.lessthan20(n%10)
        if nn < 90:
            return pre + "Eighty " + self.lessthan20(n%10)
        return pre + "Ninety " + self.lessthan20(n%10)
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        
        O = num % 1000
        T = num / 1000 % 1000
        M = num / 1000000 % 1000
        B = num / 1000000000 % 1000
        
        ans = ""
        if B != 0: 
            ans += self.toword(B).strip() + " Billion "
        if M != 0:
            ans += self.toword(M).strip() + " Million "
        if T != 0:
            ans += self.toword(T).strip() + " Thousand "
        if O != 0:
            ans += self.toword(O).strip()
        return ans.strip()