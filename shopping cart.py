cart={}
bill=0
items=['shirt','t-shirt','pants','shorts']
price=[1000,500,2000,500]
print("1 Add to cart\n2 Remove from cart\n3 View cart\n0 EXIT")
c=int(input('Enter your choice: '))
while(c!=0):
    if(c==1):
        for i in range(4):
            print(items[i],price[i])
        add=input("Enter the item to add: ")
        if add in items:
            q=int(input("Enter quantity: "))
            cart[add]=q
            t=items.index(add)
            bill=bill+q*price[t]
        else:
            print("Sorry we do not have "+add)
    elif(c==2):
        sub=input("What do you want to remove?: ")
        if sub in cart.keys():
            o=int(input("Enter quantity to remove: "))
            if o>0:
                cart[sub]=(cart[sub]-o)
            else:
                del cart[sub]
            p=items.index(sub)
            bill=bill-(o*price[p])
        else:
            print("Item is not in the cart! ")
    elif(c==3):
        for i in cart:
            print(i,':',cart[i])
    c=int(input("1 Add to cart\n2 Remove from cart\n3 View cart\n0 EXIT\nEnter Your choice: "))
for i in cart:
    print(i,':',cart[i])
print("Your Bill is: {} Rs".format(bill))
#instead of replacing value add in the shirt





