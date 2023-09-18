#WAP to calculate electricity bill according to following critera
a=int(input("Enter the unit"))
if(a<=100 and a>=0):
    print("No charges applied")
elif(a>=100 and a<=200):
    s=(a-100)*5
    print("Charge of Electricity is",s)
elif(a>=200):
    s=500+(a-200)*10
    print("Charge of electricity is",s)
else:
    print("Invalid")