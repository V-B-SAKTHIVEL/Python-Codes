def isArmstrong(n) -> bool:
    result = 0
    num = n
    while(num > 0):
        digit = int(num % 10)
        cube = digit * digit * digit
        result += cube
        num //= 10
    return result == n

print(isArmstrong(371))
