class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = sorted(coins, reverse=True)
        l = len(coins)
        if amount == 0:
            return 0
        if l == 0 or amount < coins[-1]:
            return -1

        lst = [float('inf')]

        def func(coins, a, count):
            print(lst, coins, a, count)
            if a == 0:
                lst.append(count)
                return
            if count >= lst[-1] - 1 or coins == []:
                return

            coin = coins[0]
            tmp = 0

            while tmp <= a:
                func(coins[1:], a - tmp, count)
                tmp += coin
                count += 1

        func(coins, amount, 0)
        return lst[-1] if lst[-1] != float('inf') else -1

    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = sorted(coins, reverse=True)
        l = len(coins)
        if amount == 0:
            return 0
        if l == 0 or amount < coins[-1]:
            return -1
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i-c]+1)
        print(dp)
        return -1 if dp[amount] == float('inf') else dp[amount]


if __name__ == '__main__':
    s = Solution()
    x = [186,419,83,408]
    a = 6249
    print(s.coinChange(x, a))
    print(s.coinChange2(x, a))