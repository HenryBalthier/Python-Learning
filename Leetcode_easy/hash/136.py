class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i, v in enumerate(nums):
            d[v] = 1 + d.get(v, 0)
        for i in d:
            if d[i] == 1:
                return i


if __name__ == '__main__':
    s = Solution()
    n = [1,1,2,2,3,3,32]
    print(s.singleNumber(n))