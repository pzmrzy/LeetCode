import re


class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split('=')
        coe_p = re.compile('-?\d*x')
        con_p = re.compile('-?\d+')
        left_coe = coe_p.findall(left)
        right_coe = coe_p.findall(right)
        left_con = con_p.findall(re.sub('-?\d*x', '*', left))
        right_con = con_p.findall(re.sub('-?\d*x', '*', right))

        left_con_sum = right_con_sum = 0
        for x in left_con:
            left_con_sum += int(x)
        for x in right_con:
            right_con_sum += int(x)

        left_coe_sum = right_coe_sum = 0
        for x in left_coe:
            if x == 'x': x = '1x'
            if x == '-x': x = '-1x'
            left_coe_sum += int(x[:-1])

        for x in right_coe:
            if x == 'x': x = '1x'
            if x == '-x': x = '-1x'
            right_coe_sum += int(x[:-1])

        if left_con_sum == right_con_sum and left_coe_sum == right_coe_sum:
            return "Infinite solutions"

        if left_coe_sum == right_coe_sum:
            return "No solution"

        res = (right_con_sum - left_con_sum) / (left_coe_sum - right_coe_sum)
        return "x=" + str(res)
