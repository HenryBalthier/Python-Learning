class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations == []:
            return 0
        s = sorted(citations, reverse=True)
        l = len(s)
        tmp = 0
        for i, v in enumerate(s):
            if i+1 == v:
                return v
            if i+1 < v:
                tmp = i+1
            if i+1 > v:
                return tmp
        return tmp


s = Solution()
x = [1,2,4,5,6,0]
print(s.hIndex(x))