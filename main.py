# importing modules
from tkinter import *
import pyperclip
import utils as utils

# initialize the tkinter
root = Tk()


# setup window
root.title("Password Generator")
photo = PhotoImage(file='icon.png')
root.wm_iconphoto(True, photo)
root.geometry("400x400") # "WidthxHeight"

# initialize variable
password_length = IntVar()
password_length.set(0)

password = StringVar()
password.set('')


# password generate action
def generate_password():
    length = password_length.get();
    new_password = utils.generate_password(length)
    password.set(new_password)


# password copy action
def copy_password():
    newPassword = password.get();
    pyperclip.copy(newPassword)


# window layout design
Label(root, text="Password Generator").pack(pady=5)

Label(root, text="Enter length of password:").pack(pady=5)

Entry(root, textvariable=password_length).pack(pady=5)

Button(root, text="Generate Password", command=generate_password).pack(pady=5)

Entry(root, textvariable=password, state='readonly').pack(pady=15)

Button(root, text="Copy Password", command=copy_password).pack()


# start the tkinter event loop
root.mainloop()