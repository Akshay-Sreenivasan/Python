#FInd greater number from the 3 digits given by the user------
a=int(input("Enter the first value"))
b=int(input("Enter the Second value"))
c=int(input("Enter the thrid value"))
if(a>b):
    if(a>c):
        print("First value is greater")
    else:
        print("Thrid value is greater")
elif(b>c):
    print("Second value is greater")
else:
    print("Thrid value is greater")