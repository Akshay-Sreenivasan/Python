# Print prime number series


lowervalue=int(input('Enter the low range: '))
highvalue=int(input('Enter the high range: '))

def prime(x,y):
    print('Prime numbers in range are :')
    for i in range (x,y+1):
        if i>1:
            for j in range(2,i):
                if(i%j)==0:
                    break
            else:
                print(i)
print(prime(lowervalue,highvalue))
