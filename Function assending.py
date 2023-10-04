# Implement a function that sorts a list of numbers in ascending and descending order according to the user input
lit=int(input('Enter the limit of list '))
list=[]
i=0
while (i>=0 and i<=lit):
    value=int(input('Enter the values '))
    list.append(value)
    i=i+1
def ascending(x):
    i=sorted(x)
    return i
def descending(x):
    y=sorted(x,reverse=True)
    return y
z=ascending(list)
y=descending(list)
print('original list is',list)
print ('Ac=scending Oreder of the list is',z)
print('Descending oreder of the list is',y)