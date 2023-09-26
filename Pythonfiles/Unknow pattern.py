# * * * * *
# * * * 
# * * * *
# * * * * * * *
# * * 
# * 
# * * *
# * * 
# * * * *

star=[5,3,4,7,2,1,3,2,4]
k=0
while(k<=len(star)):
    for i in range(len(star)):
        for j in range (star[k]):
            print("*",end=" ")
    print()
k=k+1
