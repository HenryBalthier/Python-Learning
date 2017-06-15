class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        c = nums.count(val)
        for i in range(c):
            nums.pop(nums.index(val))
        return len(nums)


if __name__ == '__main__':
    s = Solution
    n = [3,2,2,3]
    v = 3
    print(s.removeElement(s,n,v))