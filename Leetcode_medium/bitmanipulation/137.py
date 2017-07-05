class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for i in d:
            if d[i] == 1:
                return d[i]

s = Solution()
x = [1,1,1,2,2,2,3,3,3,4]
print(s.singleNumber(x))