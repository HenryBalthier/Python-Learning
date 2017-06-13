
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = len(flowerbed)
        for i in range(l):
            if (0 if i == 0 else flowerbed[i-1]) == flowerbed[i] ==\
                    (0 if i == l-1 else flowerbed[i+1]) == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0


if __name__ == '__main__':
    import timeit
    s = Solution
    flowerbed = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    n = 3
    print(s.canPlaceFlowers(s, flowerbed=flowerbed, n=n))
