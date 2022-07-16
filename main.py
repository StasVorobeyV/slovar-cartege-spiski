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