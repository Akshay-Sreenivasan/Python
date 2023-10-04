# create a program to convert a decimal to binary octal and hexa decimal using function
dec=int(input('Enter the number: '))
def conversion(x):
    y=bin(x)
    z=oct(x)
    hd=hex(x)
    print('The binary value of',x,'is',y)
    print('the octal value of',x,'is',z)
    print('the hexa decimal value of',x,'is',hd)
print(conversion(dec))