import random

#задайте кортеж из 10 случайных чисел
#найдите его максимальный и минимальный элемент

a = [random.randint(0, 100) for i in range(10)]
a = tuple(a)

print(a)
print("max", max(a), "min", min(a))