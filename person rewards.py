t1=int(input("Enter the time required to complete the task: "))
t2=int(input("Enter the time required to complete the task for person 2: "))
t3=int(input("Enter the time required to complete the task for person 3: "))
#considering 10hrs as the limit
if(t1>10 and t2>10 and t3>10):
    print("All people are disqualified ")
elif(t1<10 and t1<t2 and t1<t3):
    print("person 1 is the winner ")
elif(t2<10 and t2<t1 and t2<t3):
    print("person 2 is the winner ")
elif(t3<10 and t3<t2 and t3<t1):
    print("person 3 is the winner ")
elif(t1==t2 or t2==t3 or t3==t1):
    print("its a tie!")






