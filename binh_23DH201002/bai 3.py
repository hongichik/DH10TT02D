def tamgiacvuong(n):
    if n > 0:
        tamgiacvuong(n - 1)
        print('*' * n)

def tamgiacdeu(n, current=1):
    if current <= n:
        print(' ' * (n - current) + '*' * (2 * current - 1))
        tamgiacdeu(n, current + 1)

tamgiacvuong(5)
print()
tamgiacdeu(4)