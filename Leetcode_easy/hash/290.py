class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        lst = str.split()
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
    str = "d d d d"
    print(s.wordPattern(pattern, str))