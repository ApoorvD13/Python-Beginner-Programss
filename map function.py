name = ['apoorv', 'ashwini', 'gargi']
def str(s):
    if(len(s)%2==0):
        return("even string")
    else:
        return('odd string')

print(list(map(str,name)))