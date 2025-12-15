from tkinter import *
from recommender import recommender

root = Tk()

def Clicked():
    names = []

    names = recommender(e.get())

    for i in names:
        Label(root,text=i).pack(anchor="w")

e = Entry(root)
e.pack(pady=5)

b = Button(root,text="Enter",command=Clicked)
b.pack(pady=5)

label = Label(root, text="Recommended Movies:")
label.pack(pady=5)

root.mainloop()