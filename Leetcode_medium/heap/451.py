class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        import collections
        s = collections.Counter(s)
        lst = sorted(s.items(), reverse=True, key=lambda x: x[1])
        res = ''
        for i in lst:
            res += i[0] * s[i[0]]
        return res


if __name__ == '__main__':
    s = Solution()
    x = 'tree'
    print(s.frequencySort(x))