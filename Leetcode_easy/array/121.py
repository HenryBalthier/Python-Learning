class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = 0
        low = 99999
        for i, v in enumerate(prices):
            m = max(m, v - low)
            low = min(low, v)
        return m

if __name__ == '__main__':
    s = Solution
    nums =[7, 1, 5, 3, 6, 4]
    print(s.maxProfit(s, nums))