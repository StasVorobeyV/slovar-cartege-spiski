#Казино.
#Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно.
#Цифры от одного до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный,2 черный).
#Пользователю дается 5 попыток угадать номер и цвет
#(Прим. введения с  клавиатуры: 3 красный).
#В случае неудачи вывести на экран правильную комбинацию.
import random
import random

#random.randrange(start, stop, step) - возвращает случайно выбранное число из последовательности.
#random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.

#a = int(range(" 1, 10: "))
#b = input("black, red: ")

s = random.randint(1, 10)
t = random.randint(1, 2)

a = ("ВВедите число: ")
b = ("Введите цвет: ")

while True:

    if a != s and t == b:
        print("False")
    elif a == s and t != b:
        print("False")
    elif a != s and t != b:
        print("False")
    else:
        print(a == s + t == b, "победа")
        break
