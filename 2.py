stas = input("Введите текст: ")
s = []
t = 0
a = 0
for i in stas:
    if i in ("aoyeu"):
        t += 1
        s.append(i)
    elif i in ("qwrtpdrnln"):
        a += 1
print("Гласные: ", s, "Согласные: ", t)
if t == a:
    print("Все гласные буквы: ", s)