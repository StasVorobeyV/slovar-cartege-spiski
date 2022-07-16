a = ['cat', 'dog']

b = a.copy()
print(a ,b)

d = list(a)
print(a, d)

import copy

e = copy.copy(a)
print(a, e)