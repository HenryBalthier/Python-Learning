class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        def f(nums, lst):
            if lst not in res:
                res.append(lst)
            if nums == []:
                return
            for i, v in enumerate(nums):
                if i != 0 and nums[i] == nums[i-1]:
                    continue
                f(nums[i+1:], lst + [v])
            return

        f(nums, [])
        return res

s = Solution()
x = [1,2,3]
print(s.subsets(x))