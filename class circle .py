# create a circle and intialize it with radius. make two methods getArea and get Circumference inside this class
class area:
    def __init__(self,r):
        self.radius=r
    
    def area(self):
        return self.radius**2*3.14
    
    def circum(self):
        return 2*3.14*self.radius
    
num=int(input("Enter the radius: "))
cal1=area(num)
print(cal1.area())
print(cal1.circum())
