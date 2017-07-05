class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        l = len(nums)
        count = 1
        pre = None
        i = 0
        res = l
        while i < len(nums):
            if nums[i] == pre:
                count += 1
                if count > 2:
                    res -= 1
                    nums.pop(i)
                else:
                    i+=1
            else:
                pre = nums[i]
                i += 1
                count = 1

        return res, nums


s = Solution()
x = [1,1,1,1,2,2,2,3,4,5,6]
print(s.removeDuplicates(x))