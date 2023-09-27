# WAP to count number of vowels characters frrom a string
string1=input("Enter the string ")
vowels=0
for i in string1:
    if (i =='a' or i == 'e' or i=='i' or i == 'o' or i=='u'):
        vowels=vowels+1
print("Number of vowels in string is" , vowels )