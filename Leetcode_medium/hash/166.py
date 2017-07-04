class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = ''
        if numerator / denominator < 0:
            res += '-'
        if numerator % denominator == 0:
            return str(numerator//denominator)
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator//denominator) + '.'
        numerator %= denominator
        d = {}
        i = len(res)
        while numerator > 0:
            if numerator not in d.keys():
                d[numerator] = i
            else:
                i = d[numerator]
                res = res[:i] + '(' + res[i:] + ')'
                return res
            numerator *= 10
            res += str(numerator//denominator)
            numerator %= denominator
            i+=1
        return res

s = Solution()
x = 1
y = 6
print(s.fractionToDecimal(x, y))
print(x/y)