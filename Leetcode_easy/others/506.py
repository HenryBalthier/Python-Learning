class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        lst = sorted(nums, reverse=True)
        d = {}
        for i, v in enumerate(lst):
            d[v] = str(i+1)
        res = []
        for i in nums:
            if d[i] == '1':
                res.append('Gold Medal')
            elif d[i] == '2':
                res.append('Silver Medal')
            elif d[i] == '3':
                res.append('Bronze Medal')
            else:
                res.append(d[i])
        return res


s = Solution()
x = [1,2,3,4,5]
print(s.findRelativeRanks(x))