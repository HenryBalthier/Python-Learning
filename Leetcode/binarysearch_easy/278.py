# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version >= 40:
        return True
    else:
        return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right - 1:
            m = left + (right - left) // 2
            if m == 0:
                return right
            if isBadVersion(m):
                right = m
            else:
                left = m
        return right


if __name__ == '__main__':
    s = Solution()
    x = 50
    print(s.firstBadVersion(x))
