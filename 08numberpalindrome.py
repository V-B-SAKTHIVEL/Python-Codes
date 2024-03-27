def number_palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        last_digit = x % 10
        reversed_half = reversed_half * 10 + last_digit
        x //= 10

    return x == reversed_half or x == reversed_half // 10


print(number_palindrome(121))
print(number_palindrome(20))