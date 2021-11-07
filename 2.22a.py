import random
import time
komp = random.randint(1,6)
uzyt = int(input("wprowadz liczbe od 1 do 6: "))
while uzyt != komp:
    print('sproboj zgadna ponownie')
    uzyt = int(input("wprowadz liczbe od 1 do 6: "))
    if uzyt == komp:
        print('celny strzal')
        
time.sleep(10)