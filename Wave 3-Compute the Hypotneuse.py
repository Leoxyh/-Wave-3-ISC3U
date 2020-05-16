from math import sqrt


def num(answer, d):
    answer = sqrt(first_side*first_side + second_side*second_side)
    print(answer)


first_side = int(input("Enter your first side: "))
second_side = int(input("Enter your second side: "))
num(first_side, second_side)
