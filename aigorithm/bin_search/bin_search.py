from aigorithm.timewrap import cal_time

"""
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
"""


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


'''
面试题收录:
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
1. 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''


# leetcode-34求数字范围
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                """
                此时找到了目标数的位置,接下来向左右移动,寻找完整的目标数索引范围
                [5,     7,       7,     8,       8,     10]
                                         <-- current -->
                """
                left, right = mid, mid
                while left - 1 >= 0 and nums[left - 1] == target:
                    left -= 1
                while right + 1 <= len(nums) - 1 and nums[right + 1] == target:
                    right += 1
                return [left, right]
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]
