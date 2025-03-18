def isEven(s, n):
    indexDot = 0
    evenBool = False
    for i in s:
        if(i == '.'):
            indexDot = s.index(i)
            break
        else:
            num = int(i)
            if(num % 2 == 0):
                evenBool = True
    for j in range(indexDot + 1, n):
        floatNum = int(s[j])
        if(floatNum == 0):
            continue
    
        if(floatNum % 2 == 0):
            evenBool = True
        else:
            evenBool = False
    return evenBool

n = int(input("Enter the number of characters: "))
s = input("Enter the floating point string: ")

if(isEven(s, n)):
    print("EVEN")
else:
    print("ODD")
