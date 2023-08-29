cust1=[]

#0=name, 1= ac num, 2= bal
n=int(input("How many people you want to enter: "))
for i in range(n):
    cust2 = []
    name=input("Enter the customers name: ")
    cust2.append(name)
    ac=int(input('Enter the account number: '))
    cust2.append(ac)
    bal=int(input("Enter the balance: "))
    cust2.append(bal)
    cust1.append(cust2)
s=int(input("Enter account number of the cust to display: "))
for i in cust1:
    if(s in i):
        print('Name: ',i[0])
        print('Account Number: ',i[1])
        print('Balance: ',i[2])
    else:
        print('The account number you entered doesnt exist')

