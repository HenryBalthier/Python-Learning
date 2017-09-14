import random

class SortAlgo(object):
    def __init__(self, nums):
        self.nums = nums
        self.len = len(nums)

    def s1_maopao(self):
        nums = self.nums
        for i in range(self.len):
            for j in range(self.len - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    print(nums)

    def s1_maopao_jwj(self):
        nums = self.nums
        for i in range(self.len // 2):
            for j in range(i, self.len - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    print(nums)
            for j in range(self.len - 1 - i, i, -1):
                if nums[j - 1] > nums[j]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    print(nums)

    def s2_xuanze(self):
        nums = self.nums
        for i in range(self.len):
            tmp = i
            for j in range(i + 1, self.len):
                if nums[j] < nums[tmp]:
                    tmp = j
            nums[i], nums[tmp] = nums[tmp], nums[i]
            print(nums)

    def s3_chapai(self):
        nums = self.nums
        for i in range(1, self.len):
            key = nums[i]
            j = i - 1
            while j >= 0:
                if nums[j] > key:
                    nums[j + 1] = nums[j]
                    nums[j] = key
                else:
                    break
                j -= 1
            print(nums)

    def s3_chapai_2f(self):
        pass

    def s3_chapai_xr(self):
        nums = self.nums
        step = self.len // 2
        while step > 0:
            print('step =', step)
            for i in range(step, self.len):
                print(i - step, i)
                while i >= step and nums[i - step] > nums[i]:
                    nums[i], nums[i - step] = nums[i - step], nums[i]
                    i -= step
                    print(nums)
                    if i >= step:
                        print(i - step, i)
            step //= 2

    def s4_guibing(self):
        nums = self.nums




if __name__ == '__main__':
    total = 10
    lst = [i for i in range(total)]
    nums = random.sample(lst, total)
    print(nums)
    SA = SortAlgo(nums)
    SA.s3_chapai_xr()
