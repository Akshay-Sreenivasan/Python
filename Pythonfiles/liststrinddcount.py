# Write a program that takes a list of strings as input and outputs the length of each string using a while loop. 
lit=int(input("Enter the limit "))
i=1
list=[]
count=[]
while (i>=0 and i<=lit):
    a=input("Enter the strings ")
    list.append(a)
    b=len(a)
    count.append(b)
    i=i+1
print(list)
print(count)
