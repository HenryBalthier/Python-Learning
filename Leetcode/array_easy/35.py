class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            return sorted(nums).index(target)

if __name__ == '__main__':
    s = Solution
    n = [1,3,5,6]
    t = -2
    print(s.searchInsert(s,n,t))