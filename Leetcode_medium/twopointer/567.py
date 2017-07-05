class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        l1 = len(s1)
        l2 = len(s2)
        if l2 < l1:
            return False
        if l1 == 0:
            return True

        ss = sorted(s1)
        for i in range(l2 - l1 + 1):
            if sorted(s2[i:i+l1]) == ss:
                return True

        return False


s = Solution()
x = "a"
y = "a"
print(['a', 'b'] is ['b', 'a'])
print(s.checkInclusion(x, y))