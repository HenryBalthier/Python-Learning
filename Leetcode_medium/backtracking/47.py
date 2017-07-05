class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        def f(nums, lst):
            if nums == []:
                if lst not in res:
                    res.append(lst)
                return
            for i, v in enumerate(nums):
                if i != 0 and nums[i] == nums[i-1]:
                    continue
                f(nums[:i]+nums[i+1:], lst + [v])
            return

        f(nums, [])
        return res

s = Solution()
x = [-1,-1,-1,2,2,2,1,1]
print(s.permuteUnique(x))