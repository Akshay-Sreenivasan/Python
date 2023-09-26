# * * * * *
# *
# * * * * *
# * 
# *

N= int(input("Enter the limit "))
for i in range(N):
    for j in range(N):
        if(i==0 or i==N//2)  or j == 0:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()