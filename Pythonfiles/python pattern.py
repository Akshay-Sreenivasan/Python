# P
# P Y 
# P Y T 
# P Y T H
# P Y T H O 
# P T Y H O N 
# P Y T H O 
# P Y T H 
# P Y T 
# P Y 
# P

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