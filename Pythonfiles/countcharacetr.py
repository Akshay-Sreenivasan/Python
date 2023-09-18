# Write a program that takes a string as input and outputs the number of times each character appears in the string using a while loop. 
string=input("Enter the string ")
print(string)
char=input("Enter the character to be counted")
i=0
count=0
while(i<len(string)):
    if(string[i]==char):
        count=count+1
    i=i+1
print("Number of character appered is",count)