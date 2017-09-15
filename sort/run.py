from sort.algorithms import SortAlgo
import random
import time


def test1(lst, total):
    start = time.clock()
    for i in range(10000):
        nums = random.sample(lst, total)
        SA = SortAlgo(nums)
        SA.s1_maopao()
    end = time.clock()
    print('s1_maopao = %.3f s' % (end - start))


def test2(lst, total):
    start = time.clock()
    for i in range(10000):
        nums = random.sample(lst, total)
        SA = SortAlgo(nums)
        SA.s1_maopao_jwj()
    end = time.clock()
    print('s1_maopao_jwj = %.3f s' % (end - start))


def test3(lst, total):
    start = time.clock()
    for i in range(10000):
        nums = random.sample(lst, total)
        SA = SortAlgo(nums)
        SA.s2_xuanze()
    end = time.clock()
    print('s2_xuanze = %.3f s' % (end - start))


def test4(lst, total):
    start = time.clock()
    for i in range(10000):
        nums = random.sample(lst, total)
        SA = SortAlgo(nums)
        SA.s3_chapai()
    end = time.clock()
    print('s3_chapa = %.3f s' % (end - start))


def test5(lst, total):
    start = time.clock()
    for i in range(10000):
        nums = random.sample(lst, total)
        SA = SortAlgo(nums)
        SA.s3_chapai_xr()
    end = time.clock()
    print('s3_chapai_xr = %.3f s' % (end - start))


def test6(lst, total):
    start = time.clock()
    for i in range(10000):
        nums = random.sample(lst, total)
        SA = SortAlgo(nums)
        SA.s4_guibing()
    end = time.clock()
    print('s4_guibing = %.3f s' % (end - start))


def test7(lst, total):
    start = time.clock()
    for i in range(10000):
        nums = random.sample(lst, total)
        SA = SortAlgo(nums)
        SA.s5_duipai()
    end = time.clock()
    print('s5_duipai = %.3f s' % (end - start))


def test8(lst, total):
    start = time.clock()
    for i in range(10000):
        nums = random.sample(lst, total)
        SA = SortAlgo(nums)
        SA.s6_kuaipai()
    end = time.clock()
    print('s6_kuaipai = %.3f s' % (end - start))


def test9(lst, total):
    start = time.clock()
    for i in range(10000):
        nums = random.sample(lst, total)
        SA = SortAlgo(nums)
        SA.s7_count()
    end = time.clock()
    print('s7_count = %.3f s' % (end - start))


def test10(lst, total):
    start = time.clock()
    for i in range(10000):
        nums = random.sample(lst, total)
        SA = SortAlgo(nums)
        SA.s8_jishu_tong()
    end = time.clock()
    print('s8_jishu_tong = %.3f s' % (end - start))

if __name__ == '__main__':
    import multiprocessing
    total = 1000
    lst = [i for i in range(total)]
    nums = random.sample(lst, total)

    p1 = multiprocessing.Process(target=test1, args=(lst, total))
    p2 = multiprocessing.Process(target=test2, args=(lst, total))
    p3 = multiprocessing.Process(target=test3, args=(lst, total))
    p4 = multiprocessing.Process(target=test4, args=(lst, total))
    p5 = multiprocessing.Process(target=test5, args=(lst, total))
    p6 = multiprocessing.Process(target=test6, args=(lst, total))
    p7 = multiprocessing.Process(target=test7, args=(lst, total))
    p8 = multiprocessing.Process(target=test8, args=(lst, total))
    p9 = multiprocessing.Process(target=test9, args=(lst, total))
    p10 = multiprocessing.Process(target=test10, args=(lst, total))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
