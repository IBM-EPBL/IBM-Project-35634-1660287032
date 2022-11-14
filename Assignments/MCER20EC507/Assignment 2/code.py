import random
from time import sleep



while True:
    temp=int(random.randint(1,100))
    hum=int(random.randint(1,100))

    if(temp>50):
        print("-----------------------------------------")
        print("|        ALARM : HIGH TEMPERATURE       |")
        print("-----------------------------------------\n")

    elif(hum>50):
        print("-----------------------------------------")
        print("|        ALARM : HIGH HUMIDITY          |")
        print("-----------------------------------------\n")

    else:
        print("-----------------------------------------")
        print("|        ALARM : ALL OK          |")
        print("-----------------------------------------\n")


    sleep(2)
