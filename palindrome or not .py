# Cheeck wether the entered word is palindrome or not 
str1=input("Enter the word : ")
if str1==str1[::-1]:
    print("The word is palindrome")
else:
    print("The word is not a palindrome")