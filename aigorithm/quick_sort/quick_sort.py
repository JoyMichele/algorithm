from aigorithm.timewrap import cal_time
import random

"""
思路:
1. 取一个元素p,使元素p归位
    关于归位,以1~10的有序序列为例,5的有序位置就是5,也就是说在一个无序序列中,一个数字的确切有序位置是固定了的,
归位就是将一个数字放到确切的有序位置,成为有序区的一个数字.
2. 分而治之 --分治法
    列表被p分成两部分,左边都比p小,右边都比p大
3. 应用递归,分别将p左边和右边两个无序区作为新的无序序列递归归位
排序前 : 
    5 7 4 6 3 1 2 9 8
    小于的区域 | 有序数字 | 大于的区域
    2 1 4 3      5      6 7 9 8
    递归归位:
            2 1 4 3
            6 7 9 8
"""


# 快速排序 平均时间复杂度o(nlogn),最坏时间复杂度o(n^2)
@cal_time
def quick_sort(li, left, right):
    _quick_sort(li, left, right)
    return li


def _quick_sort(li, left, right):
    # 左右指针
    if left < right:
        # 进行归位
        mid = partition(li, left, right)
        # print('mid:---', mid)
        _quick_sort(li, left, mid - 1)
        _quick_sort(li, mid + 1, right)


"""
归位有两种方法: 挖坑法,指针交换法
1. 挖坑法:
    首先选定基准元素Pivot,记住这个位置index,这个位置相当于一个'坑',设置连个指针指向数列的最左最右两个元素
            index
    Pivot=5   5 | 7  4  6  3  1  2  9 | 8
            left                  <-- right
    从right指针开始,把指针位置的元素与Pivot进行对比,比Pivot大,right指针向左移动,比Pivot小就把right指向的数字填入坑中
此时right指针位置成为新的'坑',需要一个大于基准元素0的数字来填'坑'
                                index
    Pivot=5   2 | 7  4  6  3  1 | 2  9  8
            left -->            right
    right指针位置成为'坑'之后,left指针开始移动,比较是否小于Pivot,若小于,left向右移动,若大于,就把left的数字填入'坑'中
此时left遇到的大于基准元素的数字填补了小于基准元素的right留下的坑,完成了相对基准元素的大小数调换位置
               index
    Pivot=5   2  7 | 4  6  3  1 | 7  9  8
               left         <-- right
    重复挖坑填坑操作,直到左右指针相遇......
                             index
    Pivot=5   2  1 | 4  6  3 | 1  7  9  8
               left -->      right
                      index
    Pivot=5   2  1  4  6 | 3 | 6  7  9  8
                      left  <-right               
                         index
    Pivot=5   2  1  4  3 | 3 | 6  7  9  8
                         left
                         right                
    此时left与right重合,将Pivot元素数字5填入坑中,此时index左侧都是小于Pivot的数字,右侧是大于的
                 小于     index    大于
    Pivot=5   2  1  4  3 | 5 | 6  7  9  8
                         left
                         right 
                         
2. 指针交换法
    首先也是选取Pivot和left,right
    Pivot=5   5 | 7  4  6  3  1  2  9 | 8
            left                  <-- right
    从right指针开始移动,遇到小于Pivot的就停止移动,从left开始向右移动
    Pivot=5   5 | 7  4  6  3  1 | 2  9  8
            left -->            right
    left开始移动遇到大于的就停止移动,与right指针进行交换,因为我们选定了每次是right先动,所以当left停止移动时候
    表示right停止移动过了,且left和right都遇到了大小矛盾的数字,此时将left和right指指向的数字进行交换,则数字不在矛盾,继续从right开始移动
    Pivot=5   5  7 | 4  6  3  1 | 2  9  8
                left    <-->    right
                
    Pivot=5   5  2 | 4  6  3  1 | 7  9  8
                left        <-- right
                
    Pivot=5   5  2 | 4  6  3 | 1  7  9  8
                left -->     right      
                
    Pivot=5   5  2  4  6 | 3 | 1  7  9  8    
                      left<-->right 
                      
    Pivot=5   5  2  4  1 | 3 | 6  7  9  8    
                         right 
                     left --> 
    直到left与right指针相遇,此时将Pivot和left&right重合未知的数字进行交换,实现归位                    
    Pivot=5   5  2  4  1 | 3 | 6  7  9  8    
                         right
                         left
    Pivot=5   3  2  4  1 | 5 | 6  7  9  8    
                         right
                         left  
全文思路参考自CSDN文章:
https://blog.csdn.net/csdnnews/article/details/81751022
"""


# 挖坑法
def partition(li, left, right):
    # 随机选取一个基准元素,位置为初始的'坑'
    index = random.randint(left, right)
    pivot = li[index]
    # left与right相遇前
    while left < right:
        while left < right and li[right] > pivot:
            # right指针向左移动
            right -= 1
            # print('pivot', pivot)
            # print('left:', left, 'right:', right)
            # print('li:', li)
        # 将right指针对应的小于pivot的数字填入坑中
        li[index] = li[right]
        # 此时right成为新的'坑'
        index = right
        while left < right and li[left] < pivot:
            # left指针向右移动
            left += 1
            # print('pivot', pivot)
            # print('left:', left, 'right:', right)
            # print('li:', li)
        # 用大于pivot的数字进行填坑
        li[index] = li[left]
        # 新的'坑'
        index = left
    # left和right指针相遇,用基准元素填坑
    li[index] = pivot
    return index


# 挖坑法升级版
"""
一位每次遇到数字不符合要求就会挖坑在此处,且换取指针,则省略index指针,以每次结束的指针为新的'坑'
"""

def partition(li, left, right):
    # 随机选取一个基准元素
    index = random.randint(left, right)
    pivot = li[index]
    # 将基准元素放到首位,'坑'也在首位
    li[index], li[left] = li[left], li[index]
    # left与right相遇前
    while left < right:
        while left < right and li[right] > pivot:
            # right指针向左移动
            right -= 1
            # print('pivot', pivot)
            # print('left:', left, 'right:', right)
            # print('li:', li)
        # 进行填'坑',新'坑'变为了right
        li[left] = li[right]
        while left < right and li[left] < pivot:
            # left指针向右移动
            left += 1
            # print('pivot', pivot)
            # print('left:', left, 'right:', right)
            # print('li:', li)
        # 进行填'坑',新'坑'变为了left
        li[right] = li[left]
    # left和right指针相遇,用基准元素填坑
    li[left] = pivot
    return left


# 调试时将此部分和代码证print部分解除注释
# li = list(range(10))
# random.shuffle(li)
# quick_sort(li, 0, len(li) - 1)


# 指针交换法
# def partition(li, left, right):
#     # 随机选取一个基准元素
#     index = random.randint(left, right)
#     pivot = li[index]
#     # 将基准元素挪动到首位
#     li[index], li[left] = li[left], li[index]
#     # 基准元素的位置
#     index = left
#     while left < right:
#         while left < right and li[right] > pivot:
#             right -= 1
#             # print('pivot', pivot)
#             # print('left:', left, 'right:', right)
#             # print('li:', li)
#         while left < right and li[left] <= pivot:
#             left += 1
#         #     print('pivot', pivot)
#         #     print('left:', left, 'right:', right)
#         #     print('li:', li)
#         # print(li[right], '<-->', li[left])
#
#         # left 与right指针相遇时跳出循环,将pivot和指针相遇的位置进行交换
#         if left == right:
#             # print('break')
#             break
#         # 左右指针位置的数字进行交换
#         li[right], li[left] = li[left], li[right]
#     # print(li[left], '<----->', pivot)
#     # print(index, left)
#
#     # pivot和left(与right相遇时)进行交换
#     li[left], li[index] = li[index], li[left]
#     # print('left:', left, li[left])
#     return left


# li = list(range(10))
# random.shuffle(li)
# quick_sort(li, 0, len(li) - 1)


li = list(range(100000))
random.shuffle(li)
quick_sort(li, 0, len(li) - 1)
