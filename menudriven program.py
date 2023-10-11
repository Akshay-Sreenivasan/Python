d=[]
def create(k):
    for i in range(k):
        p=input("Enter the Elements: ")
        d.append(p)
    print(d)
    print(' ')
def add():
    inp=input('Enter the element to be added: ')
    d.append(inp)
    print(d)
    print(' ')
def remove():
    remve=int(input('Enter the position: '))
    d.pop(remve)
    print(d)
    print(' ')
def sortlist():
    d.sort()
    print(d)
    print(' ')
def replace():
    pick=int(input('Enter the position tho be changed: '))
    value=input('Enter the Element: ')
    d[pick]=value
    print(d)
    print(' ')

while True:
    print('Select from the list')
    print('1).Create list')
    print('2).Add Element')
    print('3).Remove Element')
    print('4).Sort')
    print('5).Replace')
    print('6).Exit')
    print(' ')
    n=int(input('Enter the choice: '))
    if n==1:
        k=int(input("Enter the limit: "))
        create(k)
    elif n==2:
        add()
    elif n==3:
        remove()
    elif n==4:
        sortlist()
    elif n==5:
        replace()
    elif n==6:
        print('****Exiting from the menu****')
        break
        