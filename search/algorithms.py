import random

class SearchAlgo(object):
    def __init__(self, nums, lst, key):
        self.nums = nums
        self.lst = lst
        self.key = key
        self.len = len(nums)

    def s1_bianli(self):
        nums = self.nums
        length = self.len
        key = self.key
        for i in range(length):
            if nums[i] == key:
                return i
        return False

    def s2_erfen(self):
        lst = self.lst
        key = self.key
        length = self.len
        low = 0
        high = length - 1
        count = 0
        while low < high:
            count += 1
            mid = int((low + high) / 2)
            if key < lst[mid]:
                high = mid - 1
            elif key > lst[mid]:
                low = mid + 1
            else:
                # 打印折半的次数
                print("count: %s" % count)
                return mid
        print("count: %s" % count)
        return False

    def s2_chazhi(self):
        lst = self.lst
        key = self.key
        length = self.len
        low = 0
        high = length - 1
        count = 0
        while low < high:
            count += 1
            mid = low + int((high - low) * (key - lst[low])/(lst[high] - lst[low]))
            if key < lst[mid]:
                high = mid - 1
            elif key > lst[mid]:
                low = mid + 1
            else:
                # 打印折半的次数
                print("count: %s" % count)
                return mid
        print("count: %s" % count)
        return False



if __name__ == '__main__':
    total = 1000
    key = 160
    lst = [i for i in range(total)]
    nums = random.sample(lst, total)
    print(lst)
    print(nums)
    sa = SearchAlgo(nums, lst, key)
    print(sa.s2_chazhi())