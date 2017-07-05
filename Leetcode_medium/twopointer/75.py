class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red = nums.count(0)
        white = nums.count(1)
        blue = nums.count(2)
        nums[:red] = [0 for _ in range(red)]
        nums[red:red+white] = [1 for _ in range(white)]
        nums[red+white:red+white+blue] = [2 for _ in range(blue)]
        return nums

s = Solution()
x = [1, 0]
print(s.sortColors(x))