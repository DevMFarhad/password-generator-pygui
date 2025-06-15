from tkinter import *
from tkinter import ttk
import pyperclip
import utils as utils

# Initialize root window
root = Tk()
root.title("Password Generator")
root.geometry("420x380")
root.configure(bg="#f2f2f2")
root.resizable(False, False)

try:
    photo = PhotoImage(file='icon.png')
    root.iconphoto(True, photo)
except:
    pass

# Center the window on screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (420 / 2))
y = int((screen_height / 2) - (380 / 2))
root.geometry(f"420x380+{x}+{y}")

# Variables
password_length = IntVar(value=12)
password = StringVar(value="")

# Fonts
font_heading = ("Helvetica", 18, "bold")
font_normal = ("Helvetica", 12)

# Password functions
def generate_password():
    length = password_length.get()
    new_password = utils.generate_password(length)
    password.set(new_password)
    copied_label.grid_remove()

def copy_password():
    pyperclip.copy(password.get())
    copied_label.grid()
    root.after(2000, copied_label.grid_remove)

# Main Frame
main_frame = Frame(root, bg="#f2f2f2", padx=20, pady=20)
main_frame.pack(fill=BOTH, expand=True)

# Title
Label(main_frame, text="Password Generator", font=font_heading, bg="#f2f2f2", fg="#333").grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Password Length
Label(main_frame, text="🔢 Password Length:", font=font_normal, bg="#f2f2f2").grid(row=1, column=0, sticky=W, pady=5)
length_spin = Spinbox(main_frame, from_=4, to=64, textvariable=password_length, font=font_normal, width=10)
length_spin.grid(row=1, column=1, sticky=E)

# Custom style
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=font_normal, padding=6, relief="flat", background="#007acc", foreground="white")
style.map("TButton", background=[("active", "#005f99"), ("disabled", "#a9a9a9")], foreground=[("disabled", "#cccccc")])

# Generate Button (Full Width)
generate_btn = ttk.Button(main_frame, text="🔄 Generate Password", command=generate_password, style="TButton")
generate_btn.grid(row=2, column=0, columnspan=2, pady=15, sticky="ew")

# Output Field
Label(main_frame, text="🔏 Generated Password:", font=font_normal, bg="#f2f2f2").grid(row=3, column=0, columnspan=2, pady=5)
password_entry = Entry(main_frame, textvariable=password, font=("Courier", 12), state='readonly', justify='center', readonlybackground="#ffffff")
password_entry.grid(row=4, column=0, columnspan=2, pady=(0, 5), ipady=4, ipadx=5, sticky='ew')

# Copied Label (initially hidden)
copied_label = Label(main_frame, text="✅ Password copied to clipboard!", font=("Helvetica", 10), fg="green", bg="#f2f2f2")
copied_label.grid(row=5, column=0, columnspan=2, pady=(0, 10))
copied_label.grid_remove()

# Copy Button (Full Width)
copy_btn = ttk.Button(main_frame, text="📋 Copy to Clipboard", command=copy_password, style="TButton")
copy_btn.grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")

# Stretch columns
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

# Footer
footer = Label(root, text="CPI © 2025", font=("Helvetica", 9), bg="#f2f2f2", fg="#888")
footer.pack(side=BOTTOM, pady=5)

# Run GUI
root.mainloop()
