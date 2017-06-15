class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = nums.count(0)
        l = len(nums)
        for i in range(l-1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)

        nums.extend([0] * n)



if __name__ == '__main__':
    s = Solution
    nums = [0, 0]
    print(s.moveZeroes(s, nums))
