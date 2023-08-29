import random as r
ls=['brave','stupid','clever','idiot']
ls2=['cat','dog','panther']
a=True
while a==True:
    p=r.choice(ls)
    t=r.randint(1,100)
    i=r.choice(ls2)
    print("Your new password is "+p+i+str(t))
    a=input("Enter true to generate another password:")
