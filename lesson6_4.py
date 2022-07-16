#dany 2 spiska
#vypolnit operacii
#1 slozhit 2 spiska
#2 dobavte el 6 na 3 poziciu
#3 udalite vse tekstovye peremennye


list1 = [4, 6, 'py', 'tell', 78]
list2 = [44, 'hello', 56, 'exept', 3]

list3 = list1 + list2
print(list3)

for i in list2:
    list1.append(i)
    print(list1)

print("теперь давай поменяем местами в список")

list1.extend(list2)
list1.insert(3, 6)
print(list1)

for i in list1:
    if type(i) is str:
        list1.remove(i)
        print(list1)

list3 = list1 + list2
list3.pop(2)
print(list3)