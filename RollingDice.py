import random   #Select ramdom choice
from tkinter import *   #import all methods from tkinter(GUI library)

root = Tk()     #initialize tkinter
root.geometry("700x450")    #page size

l1 = Label(root, font =( 'times',200))   #widget that is used to implement display boxes where you can place

def roll():
    print("Rolling Dice")
    print("\U0001F600")
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']    #Display dots on Dice
    l1.config(text = f'{random.choice(number)}{random.choice(number)}')     #Select random choice on rolling Dice
    l1.pack()
b1 = Button(root, text ="Let's Roll Dice",width = 15 ,command = roll)       #Button to roll Dice
b1.place(x =300 , y= 0 )

root.mainloop()

