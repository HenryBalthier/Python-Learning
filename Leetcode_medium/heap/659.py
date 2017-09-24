class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import collections
        if nums == []:
            return False
        left = collections.Counter(nums)
        end = collections.Counter()
        for i in nums:
            left[i] -= 1
            if end[i-1] > 0:
                end[i-1] -= 1
                end[i] += 1
            elif left[i+1] and left[i+2]:
                left[i+1] -= 1
                left[i+2] -= 1
                end[i] += 1
            else:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    x = [1, 2, 3, 3, 4, 4, 5]
    print(s.isPossible(x))