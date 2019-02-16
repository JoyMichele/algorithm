```python
设目标数为6,有序列表[1, 2, 3, 4, 5, 6, 7, 8, 9]
选取有序序列的头尾索引作为low, high指针
以两个指针为基础求出mid, 分出左右两个候选区
--- 左候选区 --- | --- 右候选区 ---
1   2   3   4   5   6   7   8   9
low            mid             high
当mid对应的值小于目标数时, 表示目标数在右候选区
使low指针指向原mid右侧第一个位置, 即low=mid+1
--- 左候选区 --- | --- 右候选区 ---
6               7       8       9
low            mid             high
mid对应的值大于目标数, 表示目标数在左候选区
使high指针指向原mid左侧第一个位置, 即high=mid-1
此时low=high=mid, 若mid对应的值等于目标数即找到
                6
           low=mid=high
```
```python
from aigorithm.timewrap import cal_time


# 二分查找 时间复杂度o(logn)
@cal_time
def bin_search(li, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if li(mid) == target:
            return mid
        elif li[mid] > target:
            bin_search(li, target, low, mid - 1)
        else:
            bin_search(li, target, mid + 1, high)
    else:
        return


# 二分查找 时间复杂度o(logn)
@cal_time
def bin_search_1(li, target):
    low = 0
    high = len(li) - 1
    while low <= high:
        # 候选区有值
        mid = (low + high) // 2
        if li[mid] == target:
            return mid
        elif li[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
```