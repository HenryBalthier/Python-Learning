class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        res = sorted(d.items(), reverse=True, key=lambda x: x[1])[:k]
        lst = []
        for i in res:
            lst.append(i[0])
        return lst


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print(s.topKFrequent(nums, k))