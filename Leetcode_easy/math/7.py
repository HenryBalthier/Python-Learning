class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        f = -1 if x < 0 else 1
        x = abs(x)

        if x > (2 << 30):
            return 0
        sum = 0
        while x:
            n = x % 10
            print(n)
            sum = sum * 10 + n
            x = x // 10
            print(x)
        if sum > (2 << 30):
            return 0
        return f * sum


if __name__ == '__main__':
    s = Solution()
    x = -1534236469
    print(s.reverse(x))