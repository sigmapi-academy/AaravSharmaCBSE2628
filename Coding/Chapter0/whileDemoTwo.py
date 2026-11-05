lb = int(input('Enter lower bound: '))
ub = int(input('Enter upper bound: '))

countOdd = 0
while lb <= ub:
    if lb % 2 != 0:
        print(lb, end = ' ')
        countOdd += 1
    
    lb += 1

if countOdd > 0:
    print(f'\nNumber of Odd values: {countOdd}')
else:
    print('upper bound value is less than lower bound')
    