class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return None

        x1 = sorted(nums)
        x2 = sorted(nums, reverse=True)

        if x1 == nums:
            return l-1
        elif x2 == nums:
            return 0

        i = 0
        y = -999999999
        while i < l:
            left = y if i == 0 else nums[i-1]
            right = y if i == l-1 else nums[i+1]
            if left < nums[i] and nums[i] > right:
                return i
            i += 1
        return None

s = Solution()
x = [1,2,6,4,5]
print(s.findPeakElement(x))