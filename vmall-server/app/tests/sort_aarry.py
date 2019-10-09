# 1、冒泡排序（Bubble Sort）
# 冒泡排序是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

# 比较相邻的元素。如果第一个比第二个大，就交换它们两个；
# 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
# 针对所有的元素重复以上的步骤，除了最后一个；
# 重复步骤1~3，直到排序完成

def bubble_sort(array):
    if not array:
        return
    alen = len(array)
    for k in range(alen - 1, 0, -1):
        for i in range(k):
            if array[i] > array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]

    return array


# 2、选择排序（Selection Sort）
# 选择排序(Selection-sort)是一种简单直观的排序算法。它的工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

# 初始状态：无序区为R[1..n]，有序区为空；
# 第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。该趟排序从当前无序区中-选出关键字最小的记录 R[k]，
# 将它与无序区的第1个记录R交换，使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
# n-1趟结束，数组有序化了。
def selection_sort(array):
    alen = len(array)
    for k in range(alen - 1):
        minVal = k
        for i in range(k + 1, alen):
            if array[i] < array[minVal]:
                minVal = i
        array[k], array[minVal] = array[minVal], array[k]

    return array


# 3、插入排序（Insertion Sort）
# 插入排序（Insertion-Sort）的算法描述是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

# 从第一个元素开始，该元素可以认为已经被排序；
# 取出下一个元素，在已经排序的元素序列中从后向前扫描；
# 如果该元素（已排序）大于新元素，将该元素移到下一位置；
# 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
# 将新元素插入到该位置后；
# 重复步骤2~5。
def insertion_sort(array):
    alen = len(array)
    for k in range(alen):
        pre_index = k - 1
        cur = k
        while (pre_index >= 0 and array[pre_index] > array[cur]):
            array[cur], array[pre_index] = array[pre_index], array[cur]
            pre_index -= 1
            cur = pre_index + 1
    return array


# 4、快排
# 快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。

# 从数列中挑出一个元素，称为 “基准”（pivot）；
# 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
# 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
import gevent
from gevent.threadpool import *
import requests
import multiprocessing
import time

pool_size = multiprocessing.cpu_count()
# pool_size = 5
pool = ThreadPool(pool_size)

# url = 'http://192.168.16.129/api/product/'
# url = 'http://192.168.16.129/api/product/'
# url = 'http://192.168.16.129/#/product?id='
url = 'https://news.cnblogs.com/n/637965/'

products = [188549,
            188550,
            189083,
            202698,
            206728,
            207991,
            234431,
            259359,
            307546,
            361348,
            395626,
            517756,
            517762,
            523961,
            598706,
            615036,
            676676,
            758086,
            840001,
            958435,
            958435,
            1074472,
            1097069,
            1098426,
            1098438,
            1110784,
            1148061,
            1254626,
            1263613,
            1290976,
            1304764,
            1333682,
            1333705,
            1371193,
            1448102,
            1471515,
            1482791
            ]


def get_product(pid):
    res = requests.get(url=url)
    print(res.status_code)


def get_content():
    res = requests.get(url=url)


start = time.time()
for _ in range(100):
    pool.spawn(get_content)

gevent.wait()
delay = time.time() - start
print(delay, 50 / delay)
