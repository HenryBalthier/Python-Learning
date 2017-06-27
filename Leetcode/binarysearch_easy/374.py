# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    n = 6
    if num > n:
        return 1
    elif num < n:
        return -1
    else:
        return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if guess(1) == 0:
            return 1
        l = 1
        r = n
        while l < r - 1:
            m = l + (r - l) // 2
            if guess(m) == 1:
                l = m
            elif guess(m) == -1:
                r = m
            elif guess(m) == 0:
                return m
        return r


if __name__ == '__main__':
    s = Solution()
    x = 10
    print(s.guessNumber(x))