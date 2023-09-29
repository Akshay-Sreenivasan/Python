# take a list with numbers as input and print the square of each numbers in list by using loop
# -------eg input[2,5,8,9]
# ------------output [4,25,64,81]"""""""""""""""global.s"
a=[2,5,8,9]
def squre():
    sq=[]
    i=0
    while(i<len(a)):
        squr=a[i]**2
        sq.append(squr)
        i=i+1
    return sq
print(squre())