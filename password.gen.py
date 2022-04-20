#importing needed imports
import math
import random
import os
import time
import re
from datetime import datetime
import os.path
import tkinter
import clipboard
from tkinter import *

#create a tkinter window
root = Tk()
root.title("Password Generator")
root.geometry("800x600")
root.configure(background='#333333')

#create a slider for the user to choose the length of the password
slider = Scale(root, from_=8, to=128, orient=HORIZONTAL, length=500, label="Password Length:")
slider.pack()

#create a checkbox for the user to choose if they want to use special characters
special_characters = IntVar()
checkbox = Checkbutton(root, text="Special Characters", variable=special_characters)
checkbox.pack()

#create a checkbox for the user to choose if they want to use numbers
numbers = IntVar()
checkbox = Checkbutton(root, text="Numbers", variable=numbers)
checkbox.pack()

#create a checkbox for the user to choose if they want to use uppercase letters
uppercase = IntVar()
checkbox = Checkbutton(root, text="Uppercase Letters", variable=uppercase)
checkbox.pack()

#create a checkbox for the user to choose if they want to use lowercase letters
lowercase = IntVar()
checkbox = Checkbutton(root, text="Lowercase Letters", variable=lowercase)
checkbox.pack()


#create a button for the user to click to generate the password
def generate_password():
    #create a list of all the characters that the user can choose from
    characters = []
    if special_characters.get() == 1:
        characters.extend(list("!@#$%^&*()_+"))
    if numbers.get() == 1:
        characters.extend(list("0123456789"))
    if uppercase.get() == 1:
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if lowercase.get() == 1:
        characters.extend(list("abcdefghijklmnopqrstuvwxyz"))

    #create a variable to store the password
    password = ""

    #create a variable to store the length of the password
    length = slider.get()

    #create a for loop to generate the password
    for i in range(length):
        password += random.choice(characters)

    #create a variable to store the clipboard
    clipboard.copy(password)

    #create a label to display the password
    label = Label(root, text=password, font=("Helvetica", 16), bg="#333333", fg="#ffffff")
    label.pack()

    #create a label saying that the password has been copied to the clipboard
    label4 = Label(root, text="Your password has been copied to the clipboard", font=("Helvetica", 16), bg="#333333", fg="#ffffff")
    label4.pack()
    
    label6 = Label(root, text="A password is strong when it has 12+ characters, has at least 1 Uppercase Letter, 1 ", font=("Helvetica", 16), bg="#333333", fg="#ffffff")
    label6.pack()

    label7 = Label(root, text="Lowercase Letter, 1 Number, and 1 Special Character", font=("Helvetica", 16), bg="#333333", fg="#ffffff")
    label7.pack()




#create button to generate the password
button = Button(root, text="Generate Password", command=generate_password)
button.pack()




#run the window when the program is run
root.mainloop()

