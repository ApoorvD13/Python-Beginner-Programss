#dictionary of account numbers, pins and balance
name={8259:['Apoorv',20932.45,2001],1845:['Aparna',76896.89,1979],1122:['Atoull',45553.67,1971],6048:['Gargi',678568.78,1998]}

def withdraw(x,y):
    if (x > y):
        print("ERROR! Insufficient Funds")
        print('Balance: ', name[ac][1])
        print("**************")
    else:
        y = y - x
        return(y)
def balance():
    print("Your Account Balance is: ", name[ac][1])
    print("***************")
def depo(x,y):
    y += x
    return(y)

#main function
ac=int(input("Enter your account number: "))
if ac in name.keys():
    print("Welcome!", name[ac][0])
    pin = int(input("Please Enter your PIN "))
    if(pin==name[ac][2]):
        ch = int(input("1.Display Balance\n2.Deposit Money\n3.Withdraw Money\n0.EXIT\nChoose an operation "))

        while(ch!=0):
            if(ch==1):
                balance()
            elif(ch==2):

                add=int(input("Enter the amount to deposit: "))
                name[ac][1]=depo(add,name[ac][1])
                print('New balance: ', name[ac][1])
                print("**************")
            elif(ch==3):

                sub=int(input("Enter the amount to withdraw: "))
                name[ac][1]=withdraw(sub,name[ac][1])
                print('New balance: ', name[ac][1])
                print("**************")

            ch = int(input("1.Display Balance\n2.Deposit Money\n3.Withdraw Money\n0.EXIT\nChoose an operation "))
    else:
        print("Invalid PIN! ")
else:
    print("The A/C Number you entered does not exist ")
