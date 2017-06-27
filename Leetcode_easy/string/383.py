class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for i in magazine:
            d[i] = 1 + d.get(i, 0)
        print(d)
        for i in ransomNote:
            if d.get(i, None):
                d[i] -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    x1 = 'aa'
    x2 = 'aba'
    print(s.canConstruct(x1, x2))