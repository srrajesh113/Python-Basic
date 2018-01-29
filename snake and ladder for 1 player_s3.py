#program to play snake and ladder
import random
c=0
while(c<=100):
    a=input("enter r to roll a dice")
    if(a=='r'):
        r=random.randint(1,6)
        c=c+r
    else:
        print("invaild option")
    print("the dice value is",r)
    print("the present place",c)
    if(c==8):
        c=37
        print("i had climed the ladder")
    if(c==11):
        c=2
        print("snake has bite")
    if(c==13):
        c=34
        print("i had climed the ladder")
    if(c==25):
        c=4
        print("snake has bite")
    if(c==38):
        c=9
        print("snake has bite")
    if(c==40):
        c=68
        print("i had climed the ladder")
    if(c==52):
        c=81
        print("i had climed the ladder")
    if(c==65):
        c=46
        print("snake has bite")
    if(c==76):
        c=97
        print("i had climed the ladder")
    if(c==89):
        c=70
        print("snake has bite")
    if(c==93):
        c=64
        print("snake has bite")
    if(c>=100):
        print("i had won the game")
