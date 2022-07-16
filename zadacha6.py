#Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра находится в
#веденном с клавиатуры слове. (Пример HjkLM- 1 пара нижнего, 1 пара верхнего), а
#также сколько всего букв в слове, сколько гласных и согласных.

text = input('Введите слово, состоящее из букв разного регистра: ')

l = 0
u = 0

for i in range(1, len(text)):
    if text[i - 1].islower() and text[i].islower():
        l += 1
    if text[i - 1].isupper() and text[i].isupper():
        u += 1

print('Количество пар верхнего регистра:', u)
print('Количество пар нижнего регистра:', l)
print('Количество букв в слове:', len(text))

n = 0
k = 0
v = []

for i in text:
    if i in ('stasVOROBEYv'):
        n += 1
        v.append(i)
    elif i in ('adrenalinLTDGibson'):
        k += 1

print('Гласные:', n, 'Согласные:', k)