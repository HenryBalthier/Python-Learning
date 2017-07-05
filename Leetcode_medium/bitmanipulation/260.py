class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        lst = []
        for i in d:
            if d[i] == 1:
                lst.append(i)
        return lst

s = Solution()
x = [1, 2, 1, 3, 2, 5]
print(s.singleNumber(x))