class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        for i in range(n):
            tmp = 9
            if i >= 1:
                for j in range(i):
                    tmp *= (9 - j)
            res += tmp
        return res
if __name__ == '__main__':
    s = Solution()
    n = 3
    print(s.countNumbersWithUniqueDigits(n))
