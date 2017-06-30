class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d ={}
        for i in s:
            d[i] = 1 + d.get(i, 0)
        lst = []
        for i in d:
            if d[i] == 1:
                lst.append(i)
        if len(lst) == 0:
            return -1
        count = 0
        for i in s:
            if i in lst:
                return count
            count += 1

s = Solution()
x = 'aabbccd'
print(s.firstUniqChar(x))