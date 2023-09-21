b=int(input("Enter the limit"))
for p in range (b+1,0,-1):
    for q in range(0,p-1):
        print("*",end=" ")
    print(" ")