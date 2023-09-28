# find words in a string which are palindrome and convert those words of each character with @
# eg:Dad said :our mother toung is malayalam------------ @@@ said : our mother toung is @@@@@@@@@
str1="my Dad said our mother toung is malayalam"
y=str1.split()
s=' '
for i in y:
    x=i[::-1]
    # print(x)
    if i.lower()==x.lower():
        # print("@"*len(i))
        s+="#"*len(i)
        s+=" "
    else:
        # print(i)
        s+=i
        s+=" "
print(s)    
