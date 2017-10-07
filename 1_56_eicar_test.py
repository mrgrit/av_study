import sys, os

fp = open('eicar.txt','rb')
fbuf = fp.read()
print(fbuf[0:3])
if fbuf[0:3] == 'X5O':
    print('Virus')
    os.remove('eicar.txt')
else :
    print('No Virus')



fp.close()
