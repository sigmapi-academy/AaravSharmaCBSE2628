# start = int(input('Enter the start value: '))
# end = int(input('Enter the end value: '))

# for i in range(start, end+1):
#     if i % 3 == 0:
#         print(i, end=' ')
        
        
# for i in range(2, 100, 2):
#     print(i, end = ', ')


# for i in range(100, 2, -2):
#     print(i, end = ', ')

# Code to find the sum of each digit, Number is entered by the user.
num = int(input('Enter any positive number: '))
if num > 0:
    sum = 0
    while num > 0:
        sum = sum + num % 10
        num = num // 10 # lower division
    print(f'Sum of digits: {sum}') 
else:
    print(f'{num} is negative or zero')