class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pattern = s
        lst = t
        if len(lst) != len(pattern):
            return False
        d = {}
        for i, v in enumerate(pattern):
            if d.get(v, False):
                if d[v] != lst[i]:
                    return False
            else:
                d[v] = lst[i]
        d = {}
        for i, v in enumerate(lst):
            if d.get(v, False):
                if d[v] != pattern[i]:
                    return False
            else:
                d[v] = pattern[i]
        return True

if __name__ == '__main__':
    s = Solution()
    pattern = "abbb"
    str = "caaa"
    print(s.isIsomorphic(pattern, str))