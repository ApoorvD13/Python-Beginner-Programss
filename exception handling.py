'''try:
    a=int(input('Enter a number: '))
    b=int(input('Enter a number: '))
    c=a+b
    print(c)
except:
    print('you cannot add an integer and a string!')'''

'''try:
    a = int(input('Enter a number: '))
    b = int(input('Enter a number: '))
    c=a/b
    print(c)
except:
    print("You cannot divide with zero")'''

try:
    a = int(input('Enter a number: '))
    b = int(input('Enter a number: '))
    if(b%5==0):
        c=a/b
        print(c)
    else:
        raise ArithmeticError
    if(a%5!=0):
        raise ValueError
except ArithmeticError:
    print('B is not a multiple of 5')
except ValueError:
    print('A is not a multiple of 5')
    