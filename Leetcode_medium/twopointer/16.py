class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        length = len(nums)
        Min = 9999999
        res = 0
        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, length - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                m = target - tmp
                if abs(m) < Min:
                    Min = abs(m)
                    res = tmp

                if m > 0:
                    l += 1
                else:
                    r -= 1
            if Min == 0:
                return res

        return res

if __name__ == '__main__':
    s = Solution()
    x = [0, 0, 0]
    t = 1
    print(s.threeSumClosest(x, t))