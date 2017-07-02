class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        l = len(nums)
        res = float('inf')
        for i in range(l - 2):
            j, k = i+1, l-1
            while j < k:
                m = nums[i] + nums[j] + nums[k]
                s = m - target
                if abs(s) < abs(res-target):
                    res = m
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    return target
        return res


s = Solution()
x = [1,1,1,0]
print(s.threeSumClosest(x, 100))