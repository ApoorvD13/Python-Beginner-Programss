import random as ra
gate=input("Do you wanna play? ")
ls=['r','p','s']
while(gate=="yes"):
    comp=ra.choice(ls)
    player=input("Enter r for rock p for paper and s for scissor: ")
    if(comp=='r' and player=='s' or comp=='p' and player=='r' or comp=='s' and player=='p' ):
        print("Sorry! you lose ")
    elif(player=='r' and comp=='s' or player=='p' and comp=='r' or player=='s' and comp=='p'):
        print("Congrats! you won! ")
    else:
        print("It's a TIE ")
    gate=input("Play again? ")