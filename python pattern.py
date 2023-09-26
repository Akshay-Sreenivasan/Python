string="PYTHON"
x=0
for i in range(0,6):
    for j in range(i):
        print(string[j],end=" ")
    print( )
for i in range(6,0,-1):
    for j in range(i):
        print(string[j],end=" ")
    print()