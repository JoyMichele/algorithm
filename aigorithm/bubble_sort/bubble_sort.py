import random
from aigorithm.timewrap import cal_time

"""
---- 无序区 ---- | ---- 有序区 ----
8 3 6 4 1 2 9 5 | 8 3 6 4 1 2 9 5
------------ 第一次冒泡 ------------
冒泡具体过程 :
3 8 6 4 1 2 9 5 |
3 6 8 4 1 2 9 5 |
3 6 4 8 1 2 9 5 |
3 6 4 1 8 2 9 5 |
3 6 4 1 2 8 9 5 |
3 6 4 1 2 8 5 9 |
将一次冒泡后无序区最大数9加到有序区
3 6 4 1 2 8 5   |               9
------------ 第二次冒泡 ------------
3 6 4 1 2 8 5   |               9
3 4 6 1 2 8 5   |               9
3 4 1 6 2 8 5   |               9
3 4 1 2 6 8 5   |               9
3 4 1 2 6 5 8   |               9
将二次冒泡后无序区最大数8加到有序区
3 4 1 2 6 5     |             8 9
                ...
每一次冒泡都将一个无序区中最大的数加到有序区
                | 1 2 3 4 5 6 8 9
"""


# 冒泡排序第一版 时间复杂度o(n^2)
@cal_time
def bubble_sort(li):
    for i in range(len(li) - 1):
        # 每循环一次就有一个无序区最大数加到有序区
        for j in range(len(li) - i - 1):
            # i 是已经进入了有序区的数量,所以无序区需要进行排序的数是数据总量-i
            if li[j] > li[j + 1]:
                # 进行换位
                li[j], li[j + 1] = li[j + 1], li[j]


li = list(range(10000))
# 打乱列表内数字的顺序
random.shuffle(li)
bubble_sort(li)
'''
当列表恰好有序时,无论是内层还是外层循环数都是没有变化的,所以应加以判断
一旦内层循环结束时没有发生数字的换位,立即终止循环,此时列表已经是有序
'''


# 冒泡排序第二版 时间复杂度o(n^2)
@cal_time
def bubble_sort_2(li):
    for i in range(len(li) - 1):
        # 每循环一次就有一个无序区最大数加到有序区
        exchange = False
        for j in range(len(li) - i - 1):
            # i 是已经进入了有序区的数量,所以无序区需要进行排序的数是数据总量-i
            if li[j] > li[j + 1]:
                # 进行换位
                li[j], li[j + 1] = li[j + 1], li[j]
                # 有数字换位时,设置交换标志位为True
                exchange = True
        if not exchange:
            # 标志位不为真的时候表示没有数字进行换位,列表已经有序
            break


bubble_sort_2(li)
