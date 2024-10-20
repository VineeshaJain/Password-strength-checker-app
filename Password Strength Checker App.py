from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Password Strength Checker')
root.configure(bg='light blue')
root.geometry('650x400')

upload = Image.open("Photo.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root, text="Enter your password!", bg='light blue')   

def check_password_strength():
    password = entry.get()
    if len(password) == 0:
        messagebox.showerror("Error", "Password cannot be empty.(Else it is not a password)")
    elif len(password) < 6:
        messagebox.showwarning("Weak Password", "Your password is too short! (Too Weak)")
    elif len(password) < 10:
        messagebox.showinfo("Golden Password", "Your password is okay-ish. (Consider adding more characters.)")
    else:
        messagebox.showinfo("Strong Password", "Your password is a legend! (Just like mine)")

label2 = Label(root, text="Enter Password:", bg='light blue')
label2.place(x=230, y=330)

entry = Entry(root, show='*')
entry.place(x=330, y=330)

button1 = Button(root, text="Check Strength", command=check_password_strength, bg='brown', fg='white')
button1.place(x=290, y=360)

root.mainloop()
