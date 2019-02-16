from aigorithm.timewrap import cal_time


# 快速排序 时间复杂度o(n^2)
# 假定一个最小数,与剩余数比较,更新最小数到有序区,再假定无序区的一个最小数,重复检索
@cal_time
def select_sort(li):
    for i in range(len(li) - 1):
        """
        设置默认最小数索引为i,i初始为0,向右进行比较,检索剩余的len(li-1)个数
        当右侧有个数更小时候,就将当前检索到的最小数进行更新
        --- 有序区 --- | --- 无序区 ---
        3(假定的最小数)    6 8 2 3 6 9 8 1 7
                        ...   2 < 3
                              2 -->
                               ...      1 < 2
                                        1 -->
        一次完整检索后将最小数1放入有序区,此时索引0位置最小数已确定,从索引1开始
        2                 6 8 2 3 6 9 8 3 7
        ...
        """
        # 最小数索引
        min_loc = i
        for j in range(i + 1, len(li)):
            # 从第i+1个数开始检索更小的数,进行最小数索引的更新
            if li[j] < li[i]:
                min_loc = j
        # 最小数索引改变,将原最小数索引与最新的索引位置数进行调换,此时最小数进入有序区
        if min_loc != i:
            li[i], li[min_loc] = li[min_loc], li[i]
