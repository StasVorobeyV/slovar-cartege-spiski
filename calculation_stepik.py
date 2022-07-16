num = int(input())

if num > 36:
    print("ошибка ввода")
if num == 0:
    print("зеленый")

if (1 <= num <= 10 or 19 <= num <= 28) and (num % 2 == 0):
    print("черный")
else:
    print("красный")

if (11 <= num <= 18 or 29 <= num <= 36) and (num % 2 == 1):
    print("красный")
else:
    print("черный")

