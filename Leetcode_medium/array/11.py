class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        i = 0
        j = len(height) - 1
        total = 0

        while i <= j:
            total = max(min(height[i], height[j]) * (j - i), total)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return total
