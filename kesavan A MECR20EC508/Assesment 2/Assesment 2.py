import random
from time import sleep
while True:
  
    t=int(random.randint(1,100))
    h=int(random.randint(1,100))

    if(t>50):
        
        print("ALARM : HIGH TEMPERATURE")

    elif(h>50):
        
        print("ALARM : HIGH HUMIDITY")
        
    else:
        
        print("ALARM : ALL OK")
       
    sleep(2)
