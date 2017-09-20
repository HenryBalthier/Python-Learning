class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p = q = 0
        ls = len(s)
        lt = len(t)
        if lt < ls or lt == 0:
            return False
        if ls == 0:
            return True
        while p < ls and q < lt:
            if s[p] == t[q]:
                p += 1
            q += 1
        return p == ls

if __name__ == '__main__':
    s = Solution()
    x = 'axc'
    t = "ahbgdc"
    print(s.isSubsequence(x, t))