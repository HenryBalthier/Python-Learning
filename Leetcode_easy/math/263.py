class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        while num % 2 == 0 and num > 1:
            num = num // 2
        while num % 3 == 0 and num > 1:
            num = num // 3
        while num % 5 == 0 and num > 1:
            num = num // 5
        return num == 1


if __name__ == '__main__':
    s = Solution()
    x = 5

    print(s.isUgly(x))