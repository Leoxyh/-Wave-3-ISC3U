import math

number = input("Enter an integer (2 or greater): ")
number = int(number)
b = 0

factor = 2
if number < 2:
    print("Invalid number")
else:

    print(f'the factor is : {number}')
    factor = 2
    while factor <= number:
        if number % factor == 0:
            print(factor)
            number = number//factor
            b += 1
        else:
            factor += 1
    if b == 1:
        print('is prime number')