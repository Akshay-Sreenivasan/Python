# create a Temperature  class make two methods
# 1.convert fahrenheit-it will take celsius and will print it into fahrenheit.
# 2.convert celsius-it will take fahrenheit and will convet it into celsius.


# ****************method1**************


# class Temperature :
#     def __init__(self,c,f):
#         self.tempc=c
#         self.tempf=f

#     def celtofahr(self):
#         return (1.8*self.tempc)+32
#     def fahrtocel(self):
#         return (self.tempf-32)*5/9
# degreec=int(input("Enter the celsius Temperature : "))
# degreef=int(input("Enter the Fahrenheit Temperature : "))
# cal1=Temperature (degreec,degreef)
# print("The temperature in fahrenheit is",cal1.celtofahr())
# print("The temperature in celsius is ",cal1.fahrtocel())

# **************************method2*******************************

class Temperature :
    def __init__(self,c):
        self.temp=c

    def celtofahr(self):
        return (1.8*self.temp)+32
    def fahrtocel(self):
        return (self.temp-32)*5/9
degree=int(input("Enter the Temperature : "))
cal1=Temperature (degree)
print("The temperature in fahrenheit is",cal1.celtofahr())
print("The temperature in celsius is ",cal1.fahrtocel())

