rome=input('Enter the Roman letter: ')
def romtoint(rom):
    roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    i = 0
    num = 0
    while i < len(rom):
        if i+1<len(rom) and rom[i:i+2] in roman:
           num+=roman[rom[i:i+2]]
           i+=2
        else:
          #print(i)
           num+=roman[rom[i]]
           i+=1
    return num
print(romtoint(rome))