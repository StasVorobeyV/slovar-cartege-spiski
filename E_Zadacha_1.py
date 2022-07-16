n = input('Введите 7-чное число: ')
n = [int(i) for i in n]
print(n)

chet = 0
nechet = 0

for i in n:
    if i % 2 == 0:
        chet += 1
    else:
        nechet += 1

print('Чётное: ', chet, 'Нечётное: ', nechet)

sum = 0
pr = 1

if chet > nechet:
    for i in n:
        sum += 1
    print(sum)
else:
    pr = n[0] * n[2] * n[5]
    print(pr)