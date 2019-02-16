斐波那契数列 :
 1 1 2 3 5 8 13 ...
 第n项的值等于第n-1项和n-2项的和

```python
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
```
面试题收录 :
1. 一段有n个台阶组成的楼梯，小明从楼梯的最底层向最高处前进，它可以选择一次迈一级台阶或者一次迈两级台阶。问：他有多少种不同的走法？
2. 有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
