#С клавиатуры вводится 7 значное число.
#Если четных цифр в нем больше, чем нечетных, то найти сумму всех его цифр
#если нечетных больше, то найти произведение 1 3 и 6 цифры.

stas = [1, 2, 3, 4 , 5, 6, 7]

vorobey1 = 0
vorobey2 = 0
for i in stas:
    if i % 2 == 0:
        vorobey1 += 1
    else:
        vorobey2 += 1
    print("Четных:", vorobey1, "нечетных:", vorobey2)
    sum = 0
    pr = 1
    if vorobey1 > vorobey2:
        for i in stas:
            sum += 2
            print("Сумма", sum)
    else:
        pr = stas[1] * stas[3] * stas[6]
        print("Произведение: ", pr)