class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        if l <= 2:
            return max(nums)

        a = 0
        b = 0
        res = 0
        print(nums)
        print(a, b)
        for i in range(l):
            a, b = res, a+nums[i]
            print(a, b, res)
            res = max(a, b)
        return res
if __name__ == '__main__':
    s = Solution()
    x = [10, 9, 0, 0, 0, 0, 0, 9]
    print(s.rob(x))