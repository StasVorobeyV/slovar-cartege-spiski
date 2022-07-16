# дается два числа
#поделите первое на второе
# обратите внимание на 0
try:
    a = int(input("Введите первое число с клавиатуры:"))
    b = int(input("Введите второе число:"))
    result = int(a)/(b)
except ZeroDivisionError:
    print("Все плохо")

else:
    print("Результат возвести в квадрат:", result**2)

finally:
    print("конец всего")