import random
computer=random.choice([-1,0,1]) 
youstr=str(input("enter your choice:"))
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"gun"}
you=youDict[youstr]
print(f"you chose:{reverseDict[you]}\ncomputer chose:{reverseDict[computer]}")
if computer==you:
    print("its a draw")
else:
    if computer==0 and you==1:
        print("you lost!")
    elif computer==0 and you==-1:
        print("you win!")
    elif computer==1 and you==-1:
        print("you lost!")
    elif computer==1 and you==0:
        print("you win!")
    elif computer==-1 and you==1:
        print("you win!")
    elif computer==-1 and you==0:
        print("you lost!")
    else:
        print("something went wrong")
    
    
    
    

            