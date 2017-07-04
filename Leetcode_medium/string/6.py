class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        d = {}
        for i in range(numRows):
            d[i] = ''
        idx = 0
        flag = 1
        l = len(s)
        for i in range(l):
            if idx == numRows-1:
                flag = -1
            elif idx == 0:
                flag = 1
            d[idx] += s[i]
            idx += flag
        res = ''
        for i in range(numRows):
            res += d[i]
        return res

s = Solution()
x = "PAYPALISHIRING"
x2 = 'AB'
print(s.convert(x2, 1))
