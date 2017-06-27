class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        l = len(s)
        lst = []
        if l == 0:
            return False
        for i in s:
            if i in d:
                lst.append(d[i])
            else:
                if len(lst) == 0:
                    return False
                elif lst[-1] != i:
                    return False
                lst.pop(-1)
        return len(lst) == 0


if __name__ == '__main__':
    s = Solution()
    x = "()[()]{}"
    print(s.isValid(x))