# a=int(input("Enter the no.of days "))
# d={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
# if(a==31):
#     print(d[1],d[3],d[5],d[7],d[8],d[10],d[12])
# elif(a==30):
#     print(d[4],d[6],d[9],d[11])
# elif(a==29 or a==28):
#     print(d[2])
# else:
#     print("Invalid!!!!Enter correctly !!!")
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
a=int(input("Enter the no.of days "))
d={31:["January","March","May","July","August","October","December"],30:["April","June","September","November"],28:"February"}
if(a==31):
    print(d[31])
elif(a==30):
    print(d[30])
elif(a==29 or a==28):
    print(d[28])
else:
    print("Invalid!!!!Enter correctly !!!")