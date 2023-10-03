# Find factorial of a number
num=int(input('Enter the number: '))
def factorial(x):
    return 1 if (x==1 or x==0) else x *factorial(x-1)
print("factorial of",num,"is",factorial(num))