class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        n -= 1
        for digits in range(1, 11):
            first = 10 ** (digits - 1)
            print(digits)
            print(first)
            print(9 * first * digits)
            print(first + n / digits)
            print('########')
            if n < 9 * first * digits:
                return int(str(first + n / digits)[n % digits])
            n -= 9 * first * digits

if __name__ == '__main__':
    s = Solution()
    x = 9
    print(s.findNthDigit(x))