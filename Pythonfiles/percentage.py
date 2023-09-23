#WAP to accept percentage
a=int(input("Enter Percentage"))
if(a>90):
    print("A Grade")
elif(a>80 and a<=90):
    print("B Grade")
elif(a>=60 and a<=80):
    print("C Grade")
elif(a<=60):
    print("D Grade")