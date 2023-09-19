# WAP to check wether the last digit of a number is divisible by three
a=int(input("Enter the value"))
x=a%10
if(x%3==0):
    print("Number is divisible by three")
else:
    print("Number is not divisible")