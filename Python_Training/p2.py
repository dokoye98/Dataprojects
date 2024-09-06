import random

health = 100
troll = 4
trollhealth  = 120
damage  = random.randrange(5)
herodam = random.randrange(7)

while health > 0:
    health -= damage
    trollhealth - herodam
    print(trollhealth,health)
    if trollhealth > 0:
         troll -=1
         print(troll)
    if troll <0:
        
        print("well done you")
        break