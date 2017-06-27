class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        s = set(candies)
        l1 = int(len(candies) / 2)
        l2 = len(s)
        return min(l1, l2)
if __name__ == '__main__':
    s = Solution
    c = [1,1,2,2,3,3]
    print(s.distributeCandies(s,c))