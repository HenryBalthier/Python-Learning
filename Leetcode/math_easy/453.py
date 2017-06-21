class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = nums
        sum = 0
        m = min(s)
        for i in s:
            sum += i - m
        return sum

if __name__ == '__main__':
    s = Solution()
    n = [5,6,8,8,5]
    print(s.minMoves(n))