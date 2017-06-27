class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0
        m = 0
        low = 999999
        for i, v in enumerate(prices):
            m = max(m, v - low)
            low = min(v, low)
            if i+1 < len(prices) and prices[i+1] < v:
                sum += m
                m = 0
                low = v
        sum +=m
        return sum
if __name__ == '__main__':
    s = Solution
    nums = [7, 1, 5, 3, 6, 4]
    print(s.maxProfit(s, nums))