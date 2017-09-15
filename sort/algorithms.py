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
        def devide(lst):
            length = len(lst)
            if length <= 1:
                return lst
            mid = length // 2
            left = devide(lst[:mid])
            right = devide(lst[mid:])
            return merge(left, right)

        def merge(left, right):
            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result += left[i:]
            result += right[j:]
            print(result)
            return result
        devide(nums)

    def s4_guibing2(self):
        pass

    def s5_duipai(self):
        def adjustheap(nums, size, root):
            left = 2 * root + 1
            right = left + 1
            tmp = root

            if left < size and nums[tmp] < nums[left]:
                tmp = left
            if right < size and nums[tmp] < nums[right]:
                tmp = right

            if tmp != root:
                nums[tmp], nums[root] = nums[root], nums[tmp]
                print(nums)
                adjustheap(nums, size, tmp)


        def buildheap(nums):
            size = len(nums)
            for i in range(size//2 - 1, -1, -1):
                adjustheap(nums, size, i)


        nums = self.nums
        length = self.len

        buildheap(nums)
        print('______________')
        for i in range(length - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            adjustheap(nums, i, 0)

    def s6_kuaipai(self):
        def quicksort(nums, left, right):
            if left >= right:
                return

            flag = nums[right]
            i = left - 1
            for j in range(left, right):
                if nums[j] <= flag:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
                    print(nums)
            nums[right], nums[i+1] = nums[i+1], nums[right]
            mid = i+1
            print('mid', nums[mid],nums)

            quicksort(nums, left, mid - 1)
            quicksort(nums, mid + 1, right)

        nums = self.nums
        length = self.len
        quicksort(nums, 0, length - 1)
        print(nums)

    def s7_count(self):
        nums = self.nums
        length = self.len
        lst = [0] * length
        res = [0] * length
        for i in nums:
            lst[i] += 1
        for i in range(length-1):
            lst[i+1] += lst[i]
        for i in range(length):
            res[lst[nums[i]-1]-1] = nums[i]
            print(res)

    def s8_jishu_tong(self):
        nums = self.nums
        length = self.len
        size = 0
        for i in nums:
            size = max(size, len(str(i)))
        print(size)





if __name__ == '__main__':
    total = 10
    lst = [i for i in range(total)]
    nums = random.sample(lst, total)
    print(nums)
    SA = SortAlgo(nums)
    SA.s8_jishu_tong()

