class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        m = nums[:]
        min = sorted(m, reverse=True)

        if min == nums:
            nums.sort()
        else:
            l = len(m)
            lst = []
            for i in range(l):
                ll = l - 1 - i
                if i == 0:
                    lst.append(nums[ll])
                else:
                    if nums[ll] >= lst[-1]:
                        lst.append(nums[ll])
                    else:
                        for j in range(len(lst)):
                            if nums[ll] < lst[j]:
                                nums[l-1-j], nums[ll] = nums[ll], nums[l-1-j]
                                nums[ll+1:] = sorted(nums[ll+1:])
                                break
                        break

        print(nums)



s = Solution()
x = [1, 3, 2]
print(s.nextPermutation(x))