import random
from time import sleep

while True:
    p=int(random.randint(1,100))
    m=int(random.randint(1,100))

    if(p>50):
        print("-----------------------------------------")
        print("|        ALARM : HIGH TEMPERATURE       |")
        print("-----------------------------------------\n")

    elif(m>50):
        print("-----------------------------------------")
        print("|        ALARM : HIGH HUMIDITY          |")
        print("-----------------------------------------\n")

    else:
        print("-----------------------------------------")
        print("|        ALARM : ALL OK          |")
        print("-----------------------------------------\n")


    sleep(2)
