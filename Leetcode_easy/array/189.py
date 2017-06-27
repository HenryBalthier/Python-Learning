class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        print(id(nums))
        nums[:] = nums[n-k:n] + nums[0:n-k]
        print(id(nums))
        return nums


if __name__ == '__main__':
    s = Solution
    nums =[1,2]
    k = 1
    print(s.rotate(s, nums, k))