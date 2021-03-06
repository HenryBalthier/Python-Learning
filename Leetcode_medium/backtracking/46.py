class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def f(nums, lst):
            if nums == []:
                res.append(lst)
                return
            for i, v in enumerate(nums):
               f(nums[:i]+nums[i+1:], lst + [v])
            return

        f(nums, [])
        return res

s = Solution()
x = [1,2,3,4]
print(s.permute(x))