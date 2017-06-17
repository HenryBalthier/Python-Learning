class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s1 = set(s)
        s2 = set(t)
        res = s2 - s1
        if len(res):
            for i in res:
                return i
        else:
            d = {}
            for i in s:
                d[i] = 1 + d.get(i, 0)
            for i in t:
                if i not in d:
                    return i
                else:
                    if d[i] == 0:
                        return i
                    else:
                        d[i] -= 1




if __name__ == '__main__':
    s = Solution()
    s1 = "abcd"
    t = "abcda"
    print(s.findTheDifference(s1,t))