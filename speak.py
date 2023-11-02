# Define a class hierachy involving animals with a method "speek". implement subclasses like "dog","cat" and "cow" with their unique speek behaviors.
class speak:
   pass
class dog(speak):
    def brak():
        print("A bark is a sound most often produced by dogs")
class cat(speak):
    def meows():
        print("Cats communicate with meows")
class cow(speak):
    def mooing():
        print("Cows communicate with each other using mooing")

while True:
    choice=int(input("Enter choice: \n 1.Voice of Dog \n 2.Voice of Cat \n 3.Voice of Cow \n 4.Close \n"))
    if choice==1:
        dog1=dog()
        print(dog.brak())
    elif choice==2:
        cat1=cat()
        print(cat.meows())
    elif choice==3:
        cow1=cow()
        print(cow.mooing())
    elif choice==4:
        break
    else:
        print('Invalid!!')
        break