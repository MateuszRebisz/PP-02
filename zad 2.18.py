x = int(input("podaj wzrost w cm: "))
stopa = round(x / 30.48,1)
cale = round(x / 2.54,1)
print(f' I am {x} tall, i.e. {stopa} feet and {cale} inches.')