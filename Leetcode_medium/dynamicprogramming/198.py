class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = []
        if nums == []:
            return 0

        l = len(nums)
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums)

        lst.append(nums[0])
        lst.append(nums[1])
        p = 1
        while p < l - 1:
            p += 1
            tmp = max(lst[:p-1]) + nums[p]
            lst.append(tmp)
            print(lst)
        return max(lst)

if __name__ == '__main__':
    s = Solution()
    x = [10, 9, 0, 0, 0, 0, 0, 9]
    print(s.rob(x))