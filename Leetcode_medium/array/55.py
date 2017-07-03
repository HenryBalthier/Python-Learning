class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = 0
        l = len(nums)
        for i in range(l):
            if d < i:
                return False
            d = max(d, nums[i] + i)
        return True

s = Solution()
x = [3,2,1,1,4]
print(s.canJump(x))