class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        if nums == []:
            return res
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        lenth = len(nums)
        l = 0
        r = lenth - 1
        while l < r:
            mid = (r - l) // 2
            print('l = %d, r = %d, mid = %d' % (l, r, mid))
            if nums[l + mid] < target:
                l = l + mid
            elif nums[l + mid] > target:
                r = l + mid
            else:
                l = r = l + mid
                if l > 0:
                    while nums[l - 1] == target:
                        l -= 1
                        if l == 0:
                            break
                if r < lenth - 1:
                    while nums[r + 1] == target:
                        r += 1
                        if r == lenth - 1:
                            break
                res = [l, r]
                break
            if mid == 0:
                if nums[r] == target:
                    res = [r, r]
                else:
                    res = [-1, -1]
                break
        return res

s = Solution()
x = [1,1]
t = 1
print(s.searchRange(x, t))