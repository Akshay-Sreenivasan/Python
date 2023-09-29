# WAF that takes a string as input and returns a new string with all special characters(eg:@%#@^$@&) removed
# -------------eg:
# ----------------string is : "abvfg@$@$#$hh"
# ----------------outputh is:abvfghh

string=input('Enter the string')
print('String before conversion:',string)
spicalchar=['!','@','#','$','%','^','&','*']
splstring=string
for i in spicalchar:
    splstring=splstring.replace(i,"")
print('string after conversion:',splstring)
# *****************OR*************
# def strg():
#     t=""
#     for i in string:
#         if i.isalpha():
#             t+=i
#             return t
# print(strg())