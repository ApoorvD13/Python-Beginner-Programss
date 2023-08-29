stac = [234, 233, 53, 6, 23, 423, 26, 346, 2342, 35]


def push():1
    el = int(input("Enter the element you want to push"))
    stac.append(el)


def pop():
    stac.pop()


choice = int(input("1. Push\n2.POP\n3.Show Top\n4.Exit"))
while choice != 4:
    if choice == 1:
        push()
    elif choice == 2:
        if len(stac) != 0:
            pop()
        else:
            print("Stack is empty!")

    elif choice == 3:
        if len(stac) != 0:
            print(stac[len(stac) - 1])
        else:
            print("Stack is empty!")

    choice = int(input("1. Push\n2.POP\n3.Show Top\n4.Exit"))
