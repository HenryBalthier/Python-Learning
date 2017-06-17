class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        lst = str.split(' ')
        d = {}
        for i, v in enumerate(pattern):
            if d.get(v, False):
                if d[v] != lst[i]:
                    return False
            else:
                d[v] = lst[i]
        return True



if __name__ == '__main__':
    s = Solution()
    pattern = "abbb"
    str = "dog cat cat dog"
    print(s.wordPattern(pattern, str))