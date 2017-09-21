class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        lst = [[nums[0], nums[0]]]
        l = len(nums)
        for i in range(1, l):
            tmp = [max(nums[i], nums[i] * lst[i-1][0], nums[i] * lst[i-1][1]), min(nums[i], nums[i] * lst[i-1][0], nums[i] * lst[i-1][1])]
            lst.append(tmp)
        lst = sorted(lst, key=lambda x: x[0], reverse=True)
        return lst[0][0]


if __name__ == '__main__':
    s = Solution()
    x = [2,3,-2,4, -1]
    print(s.maxProduct(x))