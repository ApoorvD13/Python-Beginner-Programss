name={8259:['Apoorv',20932.45,2001],1845:['Aparna',76896.89,1979],1122:['Atoull',45553.67,1971],6048:['Gargi',678568.78,1998]}

ac=int(input("Enter your account number: "))
if ac in name.keys():
    bal=name[ac]
    print("Welcome!", bal[0])
    pin = int(input("Please Enter your PIN "))
    if(pin==bal[2]):
        ch = int(input("1.Display Balance\n2.Deposit Money\n3.Withdraw Money\n0.EXIT\nChoose an operation "))
        while(ch!=0):
            if(ch==1):

                print("Your Account Balance is: ",bal[1])
                print("***************")
            elif(ch==2):
                add=int(input("Enter the amount to deposit: "))
                bal[1]+=add
                name[ac]=bal
                print('New balance: ', bal[1])
                print("**************")
            elif(ch==3):
                sub=int(input("Enter the amount to withdraw: "))
                if(sub>bal[1]):
                    print("ERROR! Insufficient Funds")
                    print('Balance: ',bal[1])
                    print("**************")
                else:
                    bal[1]=bal[1]-sub
                    name[ac]=bal
                    print('New balance: ',bal[1])
                    print("**************")
            ch = int(input("1.Display Balance\n2.Deposit Money\n3.Withdraw Money\n0.EXIT\nChoose an operation "))
    else:
        print("Invalid PIN ")
else:
    print("The A/C Number you entered does not exist ")

