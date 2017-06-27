class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        s = set(nums)
        k = abs(k)
        lst = sorted(list(s))
        if k == 0:
            for i in s:
                if nums.count(i) > 1:
                    count += 1
            return count
        for i, v in enumerate(lst):
            if v + k in s:
                count += 1
        return count



if __name__ == '__main__':
    s = Solution
    nums = [x for x in range(9999, 0, -1)]
    print(nums)
    k = 1
    print(s.findPairs(s, nums, k))