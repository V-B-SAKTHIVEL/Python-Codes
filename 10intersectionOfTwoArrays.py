from collections import Counter


def intersect(num1, num2):
    count1 = Counter(num1)
    count2 = Counter(num2)

    intersection = []

    for num in count1:
        if num in count2:
            intersection.extend([num] * min(count1[num], count2[num]))

    return intersection


num1 = [1, 2, 2]
num2 = [2, 2]
print(intersect(num1, num2))
