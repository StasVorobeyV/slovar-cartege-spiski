#клавиатуры вводится текст
#определить, сколько в нем гласных и согласных букв.
#в случае равенства вывесит на экран все гласные

word = "Python"
vowels = 0
consonants = 0
for i in word:
    letter = i.lower()
    if letter == "a" or letter == "e" or\
       letter == "i" or letter == "o" or\
       letter == "u" or letter == "y":
        vowels += 1
    else:
        consonants += 1
print("Vowels %i\nConsonants %i" % (vowels, consonants))