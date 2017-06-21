class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        res = 0
        i = 1
        m = num // 2 + 1
        while i < m:
            if num % i == 0:
                res += i
            i += 1
        print(res)
        return res == num
if __name__ == '__main__':
    s = Solution()
    x = 13466917
    print(s.checkPerfectNumber(x))