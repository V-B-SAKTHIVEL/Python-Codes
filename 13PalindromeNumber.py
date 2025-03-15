def isPalindrome(n):
    result = 0
    num = n
    while(num > 0):
        digit = int(num % 10)
        result = result * 10 + digit
        num //= 10
    return result == n

print(isPalindrome(371))
