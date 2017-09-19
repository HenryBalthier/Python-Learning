class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def xor(s):
            s = bin(s)[2:]
            while len(s) <= n:
                s = '0' + s
            res = ''
            for i in range(n):
                if s[i] == s[i+1]:
                    res += '0'
                else:
                    res += '1'
            return int(res, base=2)
        res = []
        if n == 0:
            return res
        for i in range(2 ** n):
            res.append(xor(i))
        return res


if __name__ == '__main__':
    s = Solution()
    n = 0
    print(s.grayCode(n))