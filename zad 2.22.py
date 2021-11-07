import random
import time
komp = random.randint(1,6)
uzyt = int(input("wprowadz liczbe od 1 do 6: "))
if uzyt == komp:
    print('true')
elif uzyt != komp:
    print(f'false, computer number is {komp}')
time.sleep(10)
     