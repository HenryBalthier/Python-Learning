class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = -99999
        l = len(nums)
        if l < 6:
            res = nums
        else:
            lst = sorted(nums)
            res = [lst[0], lst[1], lst[2], lst[-1], lst[-2], lst[-3]]
        for i, v1 in enumerate(res):
            for j, v2 in enumerate(res):
                for k, v3 in enumerate(res):
                    if i != j and i != k and j != k:
                       if output < v1 * v2 * v3:
                           output = v1 * v2 * v3
        return output

s = Solution()
x = [1,2,3,4, -4, -5]
print(s.maximumProduct(x))