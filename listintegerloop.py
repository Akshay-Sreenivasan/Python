# Write a program that takes two lists of integers as input and returns a list containing the common elements using a while loop. 
lit1=int(input("Enter the limit of first string "))
i=1
list1=[]
list2=[]
result=[]
while(i>=0 and i<=lit1):
    a=int(input("Enter the intergers of first list"))
    list1.append(a)
    i=i+1
while(i>=0 and i<=lit1):
    b=int(input("Enter the intergers of second list"))
    list2.append(b)
    i=i+1
k=0
while(k<len(list1)):
    if(list1[k] in list2):
        result.append(list1[k]) 
    k=k+1
print(list1)
print(list2)
print(result)