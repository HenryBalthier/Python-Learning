class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s == '0':
            return 0
        l = len(s)
        pre = ''
        way = 1
        v = 0
        for cur in s:
            tmp = way
            if cur == '0':
                way = 0
            if 10<= int(pre + cur)<= 26:
                way += v
            v = tmp
            pre = cur
        return way


s = Solution()
x = '1111'
print(s.numDecodings(x))