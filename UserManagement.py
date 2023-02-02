from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ast

root = Tk()
root.title('Yalio Holdings - Login')
root.resizable(False,False)
root.configure(bg='#343131')

#In the code below , winfo_screenwidth and winfo_screenheight methods are used to get the screen dimensions,
# and the window dimensions are set using geometry method. The x and y coordinates of the window are calculated
# such that the window will appear in the middle of the screen.
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 925
window_height = 500
x_coordinate = (screen_width/2) - (window_width/2)
y_coordinate = (screen_height/2) - (window_height/2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))



login_icon = PhotoImage(file='C:\\Users\\Aramex\\OneDrive\\Pictures\\Saved Pictures\\login.png')
Label(root,image=login_icon,border='0',bg='#343131',).place(y=50,x=50)

login_frame = Frame(root,width=350,height=390,bg='#343131')
#login_frame.config(borderwidth=5,relief='ridge')
login_frame.place(y=50,x=480)

login_label = ttk.Label(login_frame,foreground='#9bddff',background='#343131',text='Login',font=('Dubai',22,'bold'))
#login_label.grid(column=3,row=1)
login_label.place(y=50,x=5)

def on_enter(e):
    username_entry.delete(0,'end')
def on_leave(e):
    if username_entry.get()=='':
        username_entry.insert(0,'Usename or Email')

username_entry =Entry(login_frame,width=25,border=0,background='#343131',foreground='#9bddff',font=('Dubai',11))
username_entry.place(y=100,x=10)
username_entry.insert(0,'Username or Email')
Frame(login_frame,width=256,height=2,bg='white').place(y=122,x=10)
username_entry.bind('<Enter>',on_enter)
username_entry.bind('<Leave>',on_leave)


def on_enter(event):
    password_entry.delete(0, "end")
    password_entry.config(show="")

def on_leave(event):
    if not password_entry.get():
        password_entry.insert(0, "Password")
        password_entry.config(show="")

def on_entry(event):
    password_entry.config(show="*")

password_entry = Entry(
    login_frame,
    width=25,
    border=0,
    background="#343131",
    foreground="#9bddff",
    font=("Dubai", 11),
)
password_entry.place(y=150, x=10)
password_entry.insert(0, "Password")

Frame(
    login_frame,
    width=256,
    height=2,
    bg="white"
).place(y=172, x=10)

password_entry.bind("<FocusIn>", on_enter)
password_entry.bind("<FocusOut>", on_leave)
password_entry.bind("<Key>", on_entry)


Button(login_frame,width=30,pady=7,text='Login',bg='#343131',fg='white').place(x=30,y=200)

root.mainloop()