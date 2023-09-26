# *
# * 1 *
# * 1 2 *
# * 1 2 3 *
# * 1 2 *
# * 1 *
# *
a=int(input("Enter the limit "))
for i in range (1,a+1):
    for j in range(0,i+1):
        if j==i or j==0:
            print("*",end=" ")
        else:
            print(j,end=" ")
    print(" ")
for i in range(a-1,0,-1):
    for j in range(0,i+1):
        if j==0 or i==j:
            print("*",end=" ")
        else:
            print(j,end=" ")
    print()
