import math
a = input("podaj długość a ")
a = int(a)
b = input("podaj długość b ")
b = int(b)
c = input("podaj długość c ")
c = int(c)

p = 0.5*(a+b+c)
pole = math.sqrt(p*(p-a)*(p-b)*(p-c))
polec = "Pole powierzchni wynosi: {}"
print(polec.format(pole))

