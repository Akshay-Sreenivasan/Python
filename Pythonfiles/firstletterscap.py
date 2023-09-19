# Write a program that takes a list of strings as input and outputs a new list containing the same strings, but with the first letter capitalized using a while loop. 
lit=int(input("Enter the limit "))
i=0
list=[]
capital=[]
while (i>=0 and i<lit):
    a=input("Enter the strings ")
    list.append(a)
    txt=a.capitalize()
    capital.append(txt)
    i=i+1
print(list)
print(capital)