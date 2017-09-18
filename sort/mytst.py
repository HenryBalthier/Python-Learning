import random

class mytst(object):
    def __init__(self, nums):
        self.nums = nums
        self.len = len(nums)

    def maopao(self):
        nums = self.nums
        length = self.len
        for i in range(length):
            for j in range(length-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    print(nums)

    def xuanze(self):
        nums = self.nums
        length = self.len
        for i in range(length-1):
            tmp = i
            for j in range(i+1, length):
                if nums[j] < nums[tmp]:
                    tmp = j
            nums[i], nums[tmp] = nums[tmp], nums[i]
            print(nums)

    def chapai(self):
        pass

    def xier(self):
        pass

    def guibing(self):
        pass

    def duipai(self):
        pass

    def kuaipai(self):
        def quicksort(nums, l, r):
            if l >= r:
                return nums
            flag = nums[r]
            i = l - 1

            for j in range(l, r):
                if nums[j] < flag:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[r] = nums[r], nums[i + 1]
            mid = i+1
            print(nums)
            quicksort(nums, l, mid - 1)
            quicksort(nums, mid + 1, r)

        nums = self.nums
        quicksort(nums, 0, self.len - 1)

    def jishu(self):
        pass

    def tong(self):
        pass


if __name__ == '__main__':
    total = 12
    lst = [i for i in range(total)]
    nums = random.sample(lst, total)
    print(nums)
    SA = mytst(nums)
    SA.kuaipai()