from typing import Any

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import ast

login_window = Tk()
login_window.title('Yalio Holdings - Login')
login_window.overrideredirect(True)
login_window.resizable(False,False)
login_window.configure(bg='#343131')

#In the code below , winfo_screenwidth and winfo_screenheight methods are used to get the screen dimensions,
# and the window dimensions are set using geometry method. The x and y coordinates of the window are calculated
# such that the window will appear in the middle of the screen.
screen_width = login_window.winfo_screenwidth()
screen_height = login_window.winfo_screenheight()
window_width = 925
window_height = 500
x_coordinate = (screen_width/2) - (window_width/2)
y_coordinate = (screen_height/2) - (window_height/2)
login_window.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coordinate, y_coordinate))

########################################################################################################################
#code for the Main app starts here

def colour_change(button):
    button.config(bg='#c27572')
def colour_revert(button):
    button.config(bg='#343131')

def main_app_window():
    login_window.withdraw()
    main_window = Toplevel(login_window)
    main_window.title('Yalio Holdings Limited')
    main_window.geometry("600x500")
    main_window.state('zoomed')
    window_height = main_window.winfo_screenheight()
    window_width = main_window.winfo_screenwidth()
    #TAB BUTTONS HOLDING FRAME
    holder_frame = Frame(main_window,width=150,height=window_height,bg="#343131")
    holder_frame.place(y=0,x=0)
    #TAB BUTTONS
    home_button = Button(holder_frame, width=20, height=3, bg="#343131", fg="white",text='Home')
    home_button.place(y=0,x=0)
    finance_button =Button(holder_frame,width=20,height=5,bg="#343131", fg="white",text='Finance')
    finance_button.place(y=56,x=0)

    #creating a view port
    view_port = ttk.Notebook(main_window,width=window_width-150, height=200)
    view_port.place(y=100,x=150)

    #Tab style place holderr code
    s = ttk.Style()
    s.configure('Me.TFrame', background='blue')
    n = ttk.Style()
    n.configure('New.TFrame',background='red')

    #The creating the tabs
    home_tab = ttk.Frame(view_port,style='Me.TFrame')
    view_port.add(home_tab,text= "Home")

    finance_tab =ttk.Frame(view_port,style='New.TFrame')
    view_port.add(finance_tab,text = "Finance")



########################################################################################################################

#code to close login window

def close_login_window():
    login_window.destroy()

#Function to authenticate loging credentials
def user_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == 'tulio' and password == 'MACTulio95':
        main_app_window()
    elif username != 'tulio' and password != 'MACTulio95':
        messagebox.showerror('Login Failed','Username and Password are invalid')
    elif username != 'tulio':
        messagebox.showerror('Login Failed','Username not registered Contact the Admin')
    elif password != 'MACTulio95':
        messagebox.showerror('Login Failed','Incorrect Password Entered')


login_icon = PhotoImage(file='C:\\Users\\Aramex\\OneDrive\\Pictures\\Saved Pictures\\login.png')
Label(login_window,image=login_icon,border='0',bg='#343131',).place(y=50,x=50)

login_frame = Frame(login_window,width=350,height=390,bg='#343131')
login_frame.place(y=50,x=480)

login_label = ttk.Label(login_frame,foreground='#c27572',background='#343131',text='Login',font=('Dubai',22,'bold'))
login_label.place(y=55,x=5)

def on_enter(e):
    username_entry.delete(0,'end')
def on_leave(e):
    if username_entry.get()=='':
        username_entry.insert(0,'Usename or Email')

username_entry =Entry(login_frame,width=25,border=0,background='#343131',foreground='#c27572',font=('Dubai',11))
username_entry.place(y=130,x=10)
username_entry.insert(0,'Username or Email')
Frame(login_frame,width=256,height=2,bg='white').place(y=152,x=10)
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
    foreground="#c27572",
    font=("Dubai", 11),
)
password_entry.place(y=180, x=10)
password_entry.insert(0, "Password")

Frame(
    login_frame,
    width=256,
    height=2,
    bg="white"
).place(y=202, x=10)

password_entry.bind("<FocusIn>", on_enter)
password_entry.bind("<FocusOut>", on_leave)
password_entry.bind("<Key>", on_entry)


login_button = Button(login_frame,width=30,pady=7,text='Login',bg='#343131',fg='#c27572',command=user_login)
login_button.place(x=30,y=230)
login_window.bind("<Return>", lambda event: login_button.invoke())



def colour_change(event):
    close_button.config(bg='#c27572')
def colour_revert(event):
    close_button.config(bg='#343131')


close_button = Button(login_window, width=3, height=0, text='X', bg="#343131", fg="black", font=['Robotto', 10, 'bold'],command=close_login_window )
close_button.place(x=890,y=0)
close_button.config(relief="flat")
close_button.bind('<Enter>',colour_change)
close_button.bind('<Leave>',colour_revert)

login_window.mainloop()

#Code for main app starts here


