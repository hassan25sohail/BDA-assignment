from Tkinter import *
import tkMessageBox
top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)


E1 = Entry(top, bd =5)

E1.pack(side = LEFT)


L2 = Label(top, text="User Name")
L2.pack( side = LEFT)


E2 = Entry(top, bd =5)

E2.pack(side =LEFT)
def helloCallBack2():
   #entry is a text box and z is the value of it :)
   z=E1.get()
   z+=E2.get()
   tkMessageBox.showinfo( "Hello Python", "Hello"+z)

B2= Button(top, text ="Hello", command = helloCallBack2)

B2.pack(side=RIGHT)

top.mainloop()
