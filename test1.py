fil=open('xyz.txt','w')
fil.write('line number 1\nline number 2\nline number 3\nline number 4\nline number 5\nline number 6\nline number 7\nline number 8\nline number 9\nline number 10')
#fil.write('line number 1\nline number 2\nline number 3\nline number 4\nline number 5\nline number 6')
fil.close()
fil=open('xyz.txt','r')
abc=fil.readlines()
try:
    print(abc[9])
except IndexError:
    print('10th line does not exist ')
fil.close()

