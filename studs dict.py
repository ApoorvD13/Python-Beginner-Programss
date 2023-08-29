studs={'Apoorv':[50,49,45],'Gargi':[46,46,47],'Ishita':[48,42,49],'Aarya':[41,43,46]}
ch=int(input("Enter 1 to add Student\nEnter 2 to display all students\nEnter 3 to modify\nEnter 0 to exit: "))
while(ch!=0):
    if(ch==1):
        name=input("Enter the name of the Student: ")
        ls=[]
        for i in range(1,4):
            new=int(input("Enter the marks of sub: "))
            ls.append(new)
        studs[name]=ls
    elif(ch==2):
        print(studs)
        print("-------***-------***-------***-------***-------***-------")
    elif(ch==3):
        mod=input("Enter the name to modify:" ).capitalize()
        if mod in studs.keys():
            val=int(input("enter the marks to add: "))
            studs[mod].append(val)
        else:
            print("The name you entered is not in the list! ")
    ch=int(input("Enter 1 to add Student\nEnter 2 to display all students\nEnter 3 to modify\nEnter 0 to exit: "))