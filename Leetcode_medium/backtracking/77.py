class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0 or n < 1:
            return []
        if k == 1:
            return [[i+1] for i in range(n)]

        nums = [i+1 for i in range(n)]
        res = []
        def f(nums, lst, k):
            if k == 0:
                res.append(lst)
                return
            for i, v in enumerate(nums):
                f(nums[i+1:], lst+[v], k-1)
            return

        f(nums, [], k)
        return res

s = Solution()
n = 20
k = 16
print(s.combine(n, k))