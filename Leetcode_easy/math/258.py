class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        while num>9:
            res += num % 10
            num = num // 10
        res += num
        return res if res < 10 else self.addDigits(res)

if __name__ == '__main__':
    s = Solution()
    x = 38
    print(s.addDigits(x))