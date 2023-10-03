# Print the fibanocci series

lit=int(input('Enter the limit'))
def fibanocci(x):
    num1 =0
    num2=1
    count=0
    if x<=0:
        print('enter positive numbers')
    elif x ==1:
        print('Fibanocci series of ',x,':')
        print(num1)
    else:
        print("Fibonacci sequence:")
    while count < x:
       print(num1)
       numth = num1 + num2
       num1 = num2
       num2 = numth
       count += 1
print(fibanocci(lit))