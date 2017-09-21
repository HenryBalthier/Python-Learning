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
        if l == 2 or l == 3:
            return max(nums)

        lst = []
        p = 1
        lst.append([nums[0], 0])
        lst.append([nums[0], nums[1]])
        #lst.append([nums[0] + nums[2], max(nums[1], nums[2])])
        while p < l - 2:
            p += 1
            t0 = max(max(lst[i][0] for i in range(p-1)) + nums[p], max(lst[i][0] for i in range(p)))
            t1 = max(max(lst[j][1] for j in range(p-1)) + nums[p], max(lst[i][1] for i in range(p)))
            lst.append([t0, t1])
            print(lst)
        p += 1
        t0 = max(lst[i][0] for i in range(p))
        t1 = max(max(lst[j][1] for j in range(p - 1)) + nums[p], max(lst[i][1] for i in range(p)))
        lst.append([t0, t1])
        print(lst)
        return max(lst[-1])


if __name__ == '__main__':
    s = Solution()
    x = [6,3,10,8,2,10,3,5,10,5,3]
    print(s.rob(x))