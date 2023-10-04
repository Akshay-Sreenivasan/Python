# implement the pattern
# _________*
# _________1 
# _________* * 
# _________1 2
# _________* * *
# _________3 2 1
# _________* * * *
# _________1 2 3 4
# _________* * * * *
# _________5 4 3 2 1
row=5
for i in range(0,row):
    for h in range(1,i+1):
        if i%2==1:
            for j in range(1,i+1):
                print(j,end=" ")
        else:
            for j in range(0,i+1):
                print("*",end=" ")
