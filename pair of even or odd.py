# given a lis of numbers:[2,3,4,5,6],WAPP to find ad print all pairs of numbers whose product is even and sum is odd
list=[2,3,4,5,6]
even=[]
odd=[]
i=0
# k=0
while(i<len(list)):
    for k in range(0,len(list)):
        sum=list[i]+list[k]
        pro=list[i]*list[k]
        if(sum%2!=0):
            odd1=list[i],list[k]
            odd.append(odd1)
        if(pro%2==0):
            even1=list[i],list[k]
            even.append(even1)
    i=i+1
print('product is even',even)
print('sum is odd',odd)