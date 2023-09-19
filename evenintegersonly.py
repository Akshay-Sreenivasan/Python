# Write a program that takes a list of integers as input and outputs a new list containing only the even integers using a while loop.
lit=int(input("Enter the limit "))
i=0
list=[]
even=[]
while(i>=0 and i<lit):
    a=int(input("Enter the Integers"))
    list.append(a)
    i=i+1
    if(a%2==0):
        even.append(a)
print("Integer list",list)
print("list containing only the even integers",even)