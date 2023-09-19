# 4. Write a program that takes a string as input and outputs the string in reverse order using a while loop.
string=input("Enter the string")
revstring=""
count=len(string)
while(count>0):
    revstring+=string[count-1]
    count=count-1
print("Original string is",string)
print("Reversed string is",revstring)