class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r * r > num:
            r = (r + num/r) /2
            print(r)
        return r * r == num
if __name__ == '__main__':
    s = Solution()
    x = 9
    print(s.isPerfectSquare(x))