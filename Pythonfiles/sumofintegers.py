# Write a program that takes a list of integers as input and outputs the sum of the integers using a while loop. 
limit=int(input("Enter the limit of list "))
integers=[]
sum=0
element=0
i=1
while(i>=0 and i<=limit):
    a=int(input("Enter the integer values "))
    integers.append(a)
    i=i+1
while(element<len(integers)):
    sum=sum+integers[element]
    element=element+1
print("List of integers are",integers)
print("The sum of integers are",sum)