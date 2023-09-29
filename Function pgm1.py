# Write a function that takes a name as input and returns the name with all initials capitalized. for eg input=john smith,output=John Smith
name=input("Enter the name: ")
def capname():
    cap=name
    return cap
print(capname().title())