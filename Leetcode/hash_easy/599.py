class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = 99999
        n = []
        for i, v in enumerate(list1):
            if i > res:
                break
            if v in list2:
                m = i + list2.index(v)
                if m < res:
                    n = []
                    res = m
                    n.append(v)
                elif m == res:
                    n.append(v)
        return n

if __name__ == '__main__':
    s = Solution
    l1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    l2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    print(s.findRestaurant(s,l1,l2))