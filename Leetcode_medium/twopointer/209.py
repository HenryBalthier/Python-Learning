class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if sum(nums) < s:
            return 0
        length = len(nums)
        l = 0
        r = 0
        total = 0
        MIN = length + 1
        while r <= length:
            if total < s:
                if r < length:
                    total += nums[r]
                r += 1
            else:
                MIN = min(MIN, r-l)
                total -= nums[l]
                l += 1
        return MIN

s = Solution()
x = [5,1,3,5,10,7,4,9,2,8]
n = 15
print(s.minSubArrayLen(n, x))