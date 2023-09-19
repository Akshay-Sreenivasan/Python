# WAP to accept a number from 1 to 7 and display name of the day python
a=int(input("Enter the day from 1 to 7"))
d={1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",7:"Saturday",}
if(a==1):
    print(d[1])
elif(a==2):
    print(d[2])
elif(a==3):
    print(d[3])
elif(a==4):
    print(d[4])
elif(a==5):
    print(d[5])
elif(a==6):
    print(d[6])
elif(a==7):
    print(d[7])
else:
    print("Invalid!!!! Number Enter Number from One TO Seven")