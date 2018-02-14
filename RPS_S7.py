import random
c=1
while(c==1):
    option=["rock","paper","si"]
    r=random.choice(option)
    user=input("enter the choice")
    user=user.lower()
    if(user=="rock" or "paper" or "si"):
        print("the computer",r,"the user",user)
    if(user=="rock"):
        if(r=="rock"):
            print("game is tie")
        elif(r=="paper"):
            print("u lose")
        else:
            print("u win")
    if(user=="paper"):
        if(r=="rock"):
            print("u win")
        elif(r=="paper"):
            print("u tie")
        else:
            print("u lose")
    if(user=="si"):
        if(r=="rock"):
            print("u lose")
        elif(r=="paper"):
            print("u win")
        else:
            print("u tie")
    c=int(input("enter to play again press 1 or press any number to exit"))
    if(c==1):
          print("ok")
    elif(c>=2):
        c=c-2
        print("thank u")

    
          
