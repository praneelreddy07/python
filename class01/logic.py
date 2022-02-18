a = 5
b = 7

a >= b  #False
a <= b  #True

c = a > b  # False
d = a < b  #True

e = a == b  #False
f = a != b  #True

g = not e  #True

h = e and f  #False
i = e or f  #True

if e:
    print('e is true')
elif g:
    print('this one always will print')

else:
    print('e lied!')

