# WAP to accept a numb from 1-12 and display the month
# a=int(input("Enter the day from 1 to 12 "))
# d={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
# if(a==1):
#     print(d[1])
#     print("Number of Days in",d[1],"is 31days")
# elif(a==2):
#     print(d[2])
#     print("Number of Days in",d[2],"is 28/29days")
# elif(a==3):
#     print(d[3])
#     print("Number of Days in",d[3],"is 31days")
# elif(a==4):
#     print(d[4])
#     print("Number of Days in",d[4],"is 30days")
# elif(a==5):
#     print(d[5])
#     print("Number of Days in",d[5],"is 31days")
# elif(a==6):
#     print(d[6])
#     print("Number of Days in",d[6],"is 30days")
# elif(a==7):
#     print(d[7])
#     print("Number of Days in",d[7],"is 31days")
# elif(a==8):
#     print(d[8])
#     print("Number of Days in",d[8],"is 31days")
# elif(a==9):
#     print(d[9])
#     print("Number of Days in",d[9],"is 30days")
# elif(a==10):
#     print(d[10])
#     print("Number of Days in",d[10],"is 31days")
# elif(a==11):
#     print(d[11])
#     print("Number of Days in",d[11],"is 30days")
# elif(a==12):
#     print(d[12])
#     print("Number of Days in",d[12],"is 31days")
# else:
#     print("Invalid!!!! Number Enter Number from 1 -- 12 !!!")


# -----------------------------------------------------------------------------------------------------------------------
# a=input("Enter the no.of days")
# d=("January","February","March","April","May","June","July","August","September","October","November","December")
# if a in ("January","March","May","July","August","OCtober","December"):
#     print("NO of days is 31")
# elif a in("April","June","September","November"):
#     print("No of days is 30")
# elif a =="February":
#     print("No of days 28/29")
# else:
#     print("Invalid!!!! Enter correctly !!!")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a=(input("Enter the no.of days "))
d={31:["January","March","May","July","August","October","December"],30:["April","June","September","November"],28:"February"}
if(a in d[31]):
    print("31 days")
elif(a in d[30]):
    print("30 days")
elif(a in d[28]):
    print("28/29 days")
else:
    print("Invalid!!!!Enter correctly !!!")