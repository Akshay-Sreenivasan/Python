#Write a program that takes a list of strings as input and outputs a new list containing only the strings with more than five characters using a while loop
lit=int(input("Enter the limit "))
i=0
list=[]
count=[]
while (i>=0 and i<lit):
    a=input("Enter the strings ")
    list.append(a)
    b=len(a)
    i=i+1
    if(b>5):
        count.append(a)
print("Full list",list)
print("strings with more than five characters",count)
