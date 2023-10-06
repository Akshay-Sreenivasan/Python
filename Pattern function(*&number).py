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
    for p in range (0,i+1):
        print('*',end=" ")
    print()
    if(i%2!=0):
        for j in range(0,i+1):
            print(j+1,end=" ")
        print()
    else:
        for k in range(i+1,0,-1):
            print(k,end=" ")
        print()