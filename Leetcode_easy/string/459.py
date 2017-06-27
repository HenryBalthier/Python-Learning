class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = (s + s)[1: -1]
        return s in ss



if __name__ == '__main__':
    s = Solution()
    x = 'asdfasdasdfasds'
    print(s.repeatedSubstringPattern(x))