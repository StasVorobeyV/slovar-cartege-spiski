#triangle defenition/определить существование треугольника и его тип
a = int(input("side a:")) #side a/стоорона
b = int(input("side b:")) #side b/сторона
c = int(input("side c:")) #side c/сторона

if a + c > b:
    print("triangle:")
elif a + c < b:
    print("not triangle")