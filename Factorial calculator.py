from tkinter import *
w=Tk()
w.config(background='#E6FFFF')
w.geometry('300x300')
l1=Label(w,text='Number')
e1=Entry(w,width=20)
l1.grid(row=0,column=0)
e1.grid(row=0,column=1,padx=10)
def fact():
    if int(e1.get()) == 0:
        return 1
    else:
        factorial=1
        for i in range(1,int(e1.get())+1):
            factorial*=i
        e3.delete(0,END)
        e3.insert(END,factorial)
b1=Button(w,text='Calculate',command=fact).grid(row=3,column=0)
e3=Entry(w,width=20)
e3.grid(row=4,column=1)
w.mainloop()