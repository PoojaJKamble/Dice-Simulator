import random
from tkinter import *

root = Tk()
root.geometry("700x450")

l1 = Label(root, font =( 'times',200))

def roll():
    print("Rolling Dice")
    print("\U0001F600")
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text = f'{random.choice(number)}{random.choice(number)}')
    l1.pack()
b1 = Button(root, text ="Let's Roll Dice",width = 15 ,command = roll)
b1.place(x =300 , y= 0 )

root.mainloop()

