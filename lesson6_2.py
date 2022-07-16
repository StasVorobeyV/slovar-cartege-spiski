mas = [1, 2, 3, 5, 4, 6, 7]

count = 0 #произвольная переменная
count_2 = 0

for i in mas:
    if i % 2 == 0:
        count_2 += 1
    else:
        count_2 += 1

    print('Chetnyh: ', count, 'nechetnyh', count_2)

    sum = 0
    pr = 1

    if count > count_2:
        for i in mas:
            sum += i
        print("sum: ", sum)
    else:
        pr = mas[0] * mas[2] * mas[5]
        print("proizvefdenie: ", pr)
