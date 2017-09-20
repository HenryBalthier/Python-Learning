class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return length
        l = r = 0
        lst = [1]

        for i in range(1, length):
            tmp = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    tmp = max(tmp, lst[j])
            lst.append(tmp+1)
        return max(lst)



if __name__ == '__main__':
    s = Solution()
    x = [10, 9, 2, 5, 3, 7, 101, 18]
    print(s.lengthOfLIS(x))