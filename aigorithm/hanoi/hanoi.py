def hanoi(n, A, B, C):
    if n > 0:
        hanoi(n - 1, A, C, B)  # B C换位
        print('%s -> %s' % (A, C))
        hanoi(n - 1, B, A, C)  # A B换位


hanoi(4, 'A', 'B', 'C')
