class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l <= 1:
            return 0

        lst = [0] * 3
        lst[0] = 0
        lst[1] = max(0, prices[1] - prices[0])
        if l == 2:
            return lst[1]
        lst[2] = max(lst[1], prices[2] - prices[1], prices[2] - prices[0])
        if l == 3:
            return lst[2]
        for i in range(3, l):
            lst.append(max(lst[i-1], lst[i-2], lst[i-3] + max(0, prices[i] - prices[i-1])))
            print(lst)
        return lst[-1]

    def maxProfit2(self, prices):
        free = 0
        have = cool = float('-inf')
        for p in prices:
            free, have, cool = max(free, cool), max(have, free - p), have + p
            print(free, have, cool)
        return max(free, cool)


if __name__ == '__main__':
    s = Solution()
    x = [1, 2, 3, 0, 2]
    print(s.maxProfit2(x))
