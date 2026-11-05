# 0, 1, 2, 3, 6,  ... upto N terms

N = int(input('Enter number of terms: '))
a = -1
b = 0
c = 1

while N > 1:
    f = a + b + c
    print(f, end = ', ')
    a = b
    b = c
    c = f
    N -= 1

f = a + b + c
print(f)
    