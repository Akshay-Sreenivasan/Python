# . Write a program that takes a list of integers as input and outputs the largest integer in the list using a while loop
limit=int(input("Enter the limit of list "))
integers=[]
i=0
while(i>=0 and i<=limit):
    a=int(input("Enter the integer values "))
    integers.append(a)
    i=i+1
largest=integers[0]
i=0
while i<= limit:
    if integers[i] > largest:
        largest=integers[i]
    i=i+1
print("List of integers are",integers)
print("The largest of integers are",largest)