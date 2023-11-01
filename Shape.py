# Create a base class "shape"with a method "area". create derived classes "rectangle"and"circle" that inherit from "shape" and implement the "area" method.
class shape:
    def area(self):
        pass
class rectangle(shape):

    def __init__(self,length,width):
        self.length=length
        self.width=width
    def rectarea(self):
        return self.length*self.width
    
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def crcarea(self):
        return 3.14*self.radius**2

while True:
    choice=int(input("Enter choice: \n 1.Find Area of Circle \n 2.Find Area of Rectangle \n"))
    if choice==1:
        r=int(input('Enter the radius: '))
        circle=circle(r)
        circ_area=circle.crcarea()
        print('Area of circle with radius',r,'is',circ_area)
    elif choice==2:
        l=int(input('Enter the Length: '))
        w=int(input('Enter the Width: '))
        rect=rectangle(l,w)
        rec_area=rect.rectarea()
        print('Area of Rectangle with length=',l,'And width=',w,'is',rec_area)
    else:
        print('Invalid!!')
        break