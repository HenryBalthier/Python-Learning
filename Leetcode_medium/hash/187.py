class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l = len(s)
        if l < 10:
            return []

        d = {}
        for i in range(l-9):
            d[s[i:i+10]] = d.get(s[i:i+10], 0) + 1
        return [x for x in d.keys() if d[x] > 1]


s = Solution()
x = "AAAAAAAAAAA"
print(s.findRepeatedDnaSequences(x))