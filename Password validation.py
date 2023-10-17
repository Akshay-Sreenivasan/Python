''' WAP that asks the user for a password and checks if it meets the following criteria : at least 8 characters, contains at least one uppercase letter and contains at least one digit. print "valid password if the password meets the criteria and "invalid password" if it does not.'''

import re
password=input('Enter the password: ')
def validation(pas):
    if len(pas)<8:
        print('atleast 8 characters')
        return False
    if not re.search("[a-z]",pas):
        print('atleast one lowercase')
        return False
    if not re.search("[A-Z]",pas):
        print('atleast one uppercase')
        return False
    if not re.search("[0-9]",pas):
        print('atleast one number')
        return False
    return True
if validation(password):
    print('Valid Password')
else:
    print('Invalid Password')