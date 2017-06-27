class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        houses.sort()
        heaters.sort()
        heaters += [float('inf')]
        r = i = 0
        for x in houses:
            while x >= sum(heaters[i:i+2]) / 2:
                i += 1
            r = max(r, abs(x - heaters[i]))
        return r



if __name__ == '__main__':
    s = Solution()
    h = [1,2,3,5,15]
    x = [2, 30]
    print(5/2)
    print(5/2.)
    print(s.findRadius(h, x))