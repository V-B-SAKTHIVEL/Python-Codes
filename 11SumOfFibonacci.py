def fibo(n) -> int:
    if n == 0: return 0
    if n == 1: return 1

    a, b = 0, 1
    fiboTotal = a + b
    for _ in range(2, n + 1):
        c = a + b
        fiboTotal += c
        a, b = b, c
    return fiboTotal

print(fibo(4))
