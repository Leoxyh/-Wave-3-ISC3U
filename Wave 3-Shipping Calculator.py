import math


def ship(num):
    if num > 0:
        return '%.2f' % (2.95*(num-1)+10.95)
    else:
        return "error"


money = input("Enter your money: ")
money = int(money)
print(ship(money))
