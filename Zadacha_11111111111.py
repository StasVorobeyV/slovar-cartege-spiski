#С клавиатуры вводится 7 значное число.
#Если четных цифр в нем больше, чем нечетных, то найти сумму всех его цифр
#если нечетных больше, то найти произведение 1 3 и 6 цифры.
n = int(input("Вводим семизначное значение: "))

chet = 0
nechet = 0

for i in n:
    if i % 2 == 0:
        chet += 1
    else:
        nechet += 1
if chet > nechet:
    print(sum)
else:
sum = 0
pr = 1
if chet > nechet:
        for i in n:
            sum += 1
            print(sum)
        else:
            pr = a[0] * a[2] * a[5]
        print(pr)
