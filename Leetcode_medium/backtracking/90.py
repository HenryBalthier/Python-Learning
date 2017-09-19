class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = [[]]
        last = [[]]
        for i, n in enumerate(nums):
            pickFrom = ans
            if i != 0 and nums[i - 1] == n:
                pickFrom = last
            #print('pickFrom = ', pickFrom)
            last = [a + [n] for a in pickFrom]
            #print('last = ', last)
            ans += last
            # print('ans = ', ans)

        return ans



    def subsetsWithDup2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lst = [[]]
        nums = sorted(nums)

        def func(nums):
            if nums is None:
                return
            if nums not in lst:
                lst.append(nums)


        func(nums)
        return lst



if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    print(s.subsetsWithDup(nums))