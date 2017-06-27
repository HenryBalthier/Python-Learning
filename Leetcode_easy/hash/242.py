class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1 = sorted(s)
        l2 = sorted(t)
        return l1 == l2

if __name__ == '__main__':
    s = Solution()
    s2 = "anagram"
    t = "nagaram"
    print(s.isAnagram(s2, t))