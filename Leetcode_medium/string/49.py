class Solution(object):
    def groupAnagrams(self, s):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ss = [''.join(sorted(x)) for x in s]
        d = {}

        for i in range(len(s)):
            d[ss[i]] = d.get(ss[i], []) + [s[i]]
        res = []
        for i in d:
            res.append(d[i])
        return res



s = Solution()
x = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(x))