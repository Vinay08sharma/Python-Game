# ************ Stone paper & scissor game ***************


#  Will take one input from conputer and one from the user & will decide the winner 

import random

def gameWon(comp, user):
    if comp == user:
       return None
    elif comp == 'st':
        if user == 'p':
            return True
        elif user == 's':
            return False
    elif comp == 'p':
        if user == 's':
            return True
        elif user == 'st':
            return False
    elif comp == 's':
        if user == 'st':
            return True
        elif user == 'p':
            return False        
           

randNumber = random.randint(1,3)

if(randNumber == 1):
    comp = 'st'
elif(randNumber == 2):
    comp = 'p'
elif(randNumber == 3):
    comp = 's'        

user = input("Your turn, Choose between Stone(st), Paper(p) & Scissor(s): ")

result = gameWon(comp, user)

print(f"Computer chose {comp}")
if result == None:
    print("There is a tie!!!")

elif(result == True):
    print("HURRAY!!! YOU WON !!!!!")

elif(result == False):
    print("SORYY, YOU LOOSE !!!!!!!");        

