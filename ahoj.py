import random
import time

min = 20
for i in range(20):
    if(min%2 == 0):
        print(str(min),"je parne čislo")
    time.sleep(0.5)
    min +=1

for i in range(20):
    if(min%2 > 0):
        print(str(min),"je neparne čislo")
    time.sleep(0.5)
    min +=1
