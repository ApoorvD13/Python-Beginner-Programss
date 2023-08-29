'''studs={1:'apoorv',2:'rahul',3:'yash',4:'khushi'}
print(studs)
print(studs[3])
studs[34]='prasad'
print(studs)
print(studs.keys())
print(studs.values())'''
fruits={'apple':[50,100,200],'oranges':[30,60,120],'bananas':[20,25,30],'mangoes':[200,300,500]}

ch=int(input("Enter 1 to add fruit, Enter 2 to view items in stock, Enter 3 to modify , Enter 0 to exit: "))
while(ch!=0):
    if(ch==1):
        name=input("Enter the name of the fruit: ")
        ls=[]
        n=int(input("Enter the number of qualities you want to enter: "))
        for i in range(0,n+1):
            print(i + 1, end='')
            a=input("Enter the cost of quality number ")

            ls.append(a)
        fruits[name]=ls
    elif(ch==2):
        print(fruits)
    elif(ch==3):
        mod=input("Enter the fruit to modify:" )
        if mod in fruits.keys():
            val=int(input("enter the value to add: "))
            fruits[mod].append(val)
        else:
            print("The fruit you entered is not in the list! ")
    ch=int(input("Enter 1 to add fruit, Enter 2 to view items in stock, Enter 3 to modify , Enter 0 to exit: "))






