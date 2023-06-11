#Guese the number practise

import random

flag = True

num = random.randint(1,10)


while flag == True:
    
    guese = int(input("Guese number 1-10"))

    if int(guese) < num:
        print("Too low try again")
    elif int(guese) > num:
        print(" Too high try again")
    else: 
        print(" Well done")
        flag=False




