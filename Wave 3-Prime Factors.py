import math

number = input("Enter an integer (2 or greater): ")
number = int(number)
a = 0

n = 2
if number < 2:
    print("Invalid number")
else:

    print(f'the factor is : {number}')
    n = 2
    while n <= number:
        if number % n == 0:
            print(n)
            number = number//n
            a += 1
        else:
            n += 1
    if a == 1:
        print('is prime number')