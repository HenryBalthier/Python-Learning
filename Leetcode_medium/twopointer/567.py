class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        import collections
        l1 = len(s1)
        l2 = len(s2)
        if l2 < l1:
            return False
        if l1 == 0:
            return True

        s1 = sorted(s1)
        c1, c2 = collections.Counter(s1), collections.Counter(s2)
        print(c1, c2, len(c1), len(c2))
        d = {'a': 1}
        c = {'a': 1, 'c': 2}
        print(c1 - c2)
        for i in range(l2 - l1 + 1):
            if s2[i:i+l1] == s1:
                return True
        return False



s = Solution()
x = "bca"
y = "bbbca"
print(s.checkInclusion(x, y))
