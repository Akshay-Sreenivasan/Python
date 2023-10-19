# -*********************************************akshay@leetcode123.com****************************************
num=int(input('Enter the integer '))
def square(x):
    if (x==0):
        return 0
    start=1
    end=x/2+1
    while(start<=end):
        mid=start+(end-start)/2
        if(mid==x/mid):
            return mid
        elif(mid<x/mid):
            start=mid+1
        else:
            end=mid-1
        return end
    
print('Square root of',num,'is',square(num))