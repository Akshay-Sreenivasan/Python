# Consider the following list of numbers [3,8,12,7,6,10,21,15]. WAPP to find and print all pairs of numbers whose sum is equal to 18. ???
list=[3,8,12,7,6,10,21,15]
pairlist=[]
i=0
k=0
while(i<len(list)):
    for k in range(0,len(list)):
        sum=list[i]+list[k]
        if(sum==18):
            pair=list[i],list[k]
            pairlist.append(pair)   
    i=i+1
print(pairlist)