"""
斐波那契数列 :
 1 1 2 3 5 8 13...
 第n项的值等于第n-1项和n-2项的和
"""


# 递归 时间复杂度o(2^n)
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# 非递归 时间复杂度o(n)
def fib_1(n):
    res = [1, 1]
    for i in range(2, n + 1):
        res.append(res[-1] + res[-2])
    return res[-1]


def fib_2(n):
    if n == 0 or n == 1:
        return 1
    a, b, c = 1, 1, 0
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return c
