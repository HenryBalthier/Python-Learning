class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        begin = nums[0]
        end = nums[0]
        for i, v in enumerate(nums):
            if i == 0:
                continue
            if v == nums[i-1] + 1:
                end = v
            else:
                if begin != end:
                    res.append(str(begin) + '->' + str(end))
                else:
                    res.append(str(end))
                begin = end = v
        if begin != end:
            res.append(str(begin) + '->' + str(end))
        else:
            res.append(str(end))

        return res


if __name__ == '__main__':
    s = Solution()
    nums = [0,2,3,4,6,8,9]
    print(s.summaryRanges(nums))