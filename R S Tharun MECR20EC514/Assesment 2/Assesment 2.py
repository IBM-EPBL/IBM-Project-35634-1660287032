import random
from time import sleep
while True:
    t=int(random.randint(1,100))
    h=int(random.randint(1,100))

    if(t>50):
        print("-----------------------------------------")
        print("|        ALARM : HIGH TEMPERATURE       |")
        print("-----------------------------------------\n")

    elif(h>50):
        print("-----------------------------------------")
        print("|        ALARM : HIGH HUMIDITY          |")
        print("-----------------------------------------\n")

    else:
        print("-----------------------------------------")
        print("|        ALARM : ALL OK          |")
        print("-----------------------------------------\n")


    sleep(2)
