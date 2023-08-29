import random as r
a=r.randint(1,10)
n=0
x = input("Do you want to play? ")

while(x=='yes'):

    n = int(input("Guess a Number(1-10): "))
    if(n<a):
        print("The number you guessed is too low ")
    elif(n>a):
        print("The number you guessed is too high ")
    elif(n==a):
        print("CONGRATS! you won")
        break

    #x=input("Try Again? " )
