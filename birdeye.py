from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
import mysql.connector
import re
#from tkinter import messagebox

###########################################################################################################
#Database Management Code
#Creating database connection

class employee_database:
    def __init__(self,host, user,password,database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
    def add_employee(self,data):
        insert_query = "INSERT INTO employees (firstname,middlename,lastname,dateofbirth,gender,maritalstatus,natidnumber,country,district,company,department,mobilephone1,mobilephone2,emailaddress,physicaladdress,spousename,spousecontact,children,jobposition,contracttype,startdate,enddate,basicpay,hourlyrate,overtime,bankaccount,bank) ""VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (data['firstname'], data['middlename'], data['lastname'], data['dateofbirth'], data['gender'], data['maritalstatus'], data['natidnumber'], data['country'], data['district'], data['company'], data['department'], data['mobilephone1'], data['mobilephone2'], data['emailaddress'], data['physicaladdress'], data['spousename'], data['spousecontact'], data['children'], data['jobposition'], data['contracttype'], data['startdate'], data['enddate'], data['basicpay'], data['hourlyrate'], data['overtime'], data['bankaccount'], data['bank'])
        self.cursor.execute(insert_query, values)
        self.connection.commit()
        pass

    def retrieve_data(self, row_id=None, columns=None):
        """
        Retrieve data from the "employees" table in the database.

        Parameters:
            row_id (int): The id of the row to retrieve. If None, all rows will be retrieved.
            columns (list): The list of columns to retrieve. If None, all columns will be retrieved.

        Returns:
            list of tuples: The retrieved data.
        """
        if row_id is not None:
            query = f"SELECT * FROM employees WHERE id = {row_id}"
        else:
            query = "SELECT * FROM employees"

        if columns is not None:
            columns_str = ", ".join(columns)
            query = query.replace("*", columns_str)

        self.cursor.execute(query)
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

###########################################################################################################
#Function For Notification window
def notification_bar(window_name,message,status):
    notification_window = tk.Toplevel()
    x = window_name.winfo_x()
    y = window_name.winfo_y()
    z = window_name.winfo_width()
    notification_window.geometry("{}x30+{}+{}".format(z-5,x + 10, y + 30))
    notification_window.overrideredirect(True)
    if status == "good":
        notification_window.configure(bg='#17A589')
        notification_label = tk.Label(notification_window, text=message, bg='#17A589', font=['Calibri (Body)', 15],
                                      fg='white')
        notification_label.pack()
    elif status == 'bad':
        notification_window.configure(bg='#E74C3C')
        notification_label = tk.Label(notification_window, text=message, bg='#E74C3C', font=['Calibri (Body)', 15],
                                      fg='white')
        notification_label.pack()

    notification_window.after(1500, notification_window.withdraw)

#Home buttons colour change functions
def colour_change(button):
    button.config(bg='#c27572')
def colour_revert(button):
    button.config(bg='#343131')


def on_entry_focus(e, entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, 'end')

def on_entry_blur(e, entry, default_text):
    if entry.get() == '':
        entry.insert(0, default_text)

#login_window.withdraw()
#main_window = Toplevel(login_window)

main_window = Tk()
main_window.title('Yalio Holdings Limited')
main_window.geometry("600x500")
main_window.state('zoomed')
window_height = main_window.winfo_screenheight()
window_width = main_window.winfo_screenwidth()
#TAB BUTTONS HOLDING FRAME
holder_frame = Frame(main_window,width=150,height=window_height,bg="#343131")
holder_frame.place(y=0,x=0)

#Defining Functions for Tab Selection

def show_home():
    view_port.select(home_tab)

def show_finance():
    view_port.select(finance_tab)

def show_inventory():
    view_port.select(inventory_tab)

def show_employees():
    view_port.select(employees_tab)
    employees_view_port.select(employees_dashboard)

def show_customers():
    view_port.select(customers_tab)

def show_reports():
    view_port.select(reports_tab)

def show_settings():
    view_port.select(settings_tab)

#TAB BUTTONS
home_button = Button(holder_frame, width=18, height=3, bg="#343131", fg="white",text='Home',font=['Calibri (Body)', 10, 'bold'],command=show_home)
home_button.place(y=0,x=0)
home_button.config(relief="flat")
home_button.bind('<Enter>', lambda event, button=home_button: colour_change(button))
home_button.bind('<Leave>',lambda event,button =home_button: colour_revert(button))

finance_button =Button(holder_frame,width=18,height=5,bg="#343131", fg="white",text='Finance',font=['Calibri (Body)', 10, 'bold'],command=show_finance)
finance_button.place(y=56,x=0)
finance_button.config(relief="flat")
finance_button.config(justify="center", anchor="center")
finance_button.bind('<Enter>', lambda event, button=finance_button: colour_change(button))
finance_button.bind('<Leave>',lambda event,button =finance_button: colour_revert(button))

inventory_button =Button(holder_frame,width=18,height=5,bg="#343131", fg="white",text='Inventory',font=['Calibri (Body)', 10, 'bold'],command=show_inventory)
inventory_button.place(y=145,x=0)
inventory_button.config(relief="flat")
inventory_button.config(justify="center", anchor="center")
inventory_button.bind('<Enter>', lambda event, button=inventory_button: colour_change(button))
inventory_button.bind('<Leave>',lambda event,button =inventory_button: colour_revert(button))

employees_button =Button(holder_frame,width=18,height=5,bg="#343131", fg="white",text='Employees',font=['Calibri (Body)', 10, 'bold'],command=show_employees)
employees_button.place(y=234,x=0)
employees_button.config(relief="flat")
employees_button.config(justify="center", anchor="center")
employees_button.bind('<Enter>', lambda event, button=employees_button: colour_change(button))
employees_button.bind('<Leave>',lambda event,button =employees_button: colour_revert(button))

customer_button =Button(holder_frame,width=18,height=5,bg="#343131", fg="white",text='Customers',font=['Calibri (Body)', 10, 'bold'],command=show_customers)
customer_button.place(y=323,x=0)
customer_button.config(relief="flat")
customer_button.config(justify="center", anchor="center")
customer_button.bind('<Enter>', lambda event, button=customer_button: colour_change(button))
customer_button.bind('<Leave>',lambda event,button =customer_button: colour_revert(button))

reports_button =Button(holder_frame,width=18,height=5,bg="#343131", fg="white",text='Reports',font=['Calibri (Body)', 10, 'bold'],command=show_reports)
reports_button.place(y=415,x=0)
reports_button.config(relief="flat")
reports_button.config(justify="center", anchor="center")
reports_button.bind('<Enter>', lambda event, button=reports_button: colour_change(button))
reports_button.bind('<Leave>',lambda event,button =reports_button: colour_revert(button))


#Special settings button with an Icon

tool_tip = Label(holder_frame, text="",bg="#343131",fg='white')


def show_tooltip(event):
    tool_tip.config(text='Settings')
    tool_tip.place(y=680, x=50)

settings_icon = PhotoImage(file="C:\\Users\\Aramex\\OneDrive\\Pictures\\Saved Pictures\\settings.png")
settings_button =Button(holder_frame,image=settings_icon,command=show_settings,bg="#343131",bd=0,activebackground='#343131')
settings_button.place(y=600,x=35)
settings_button.config(relief="flat")
settings_button.config(justify="center", anchor="center")
settings_button.bind("<Enter>", show_tooltip)
settings_button.bind("<Leave>", lambda event: tool_tip.config(text=""))

#creating a view port
view_port = ttk.Notebook(main_window, width=window_width-150, height=800)
view_port.place(y=10, x=150)

#Tab style place holderr code
s = ttk.Style()
s.configure('Me.TFrame', background='blue')
n = ttk.Style()
n.configure('New.TFrame',background='red')

#creating viewport tabs
home_tab = ttk.Frame(view_port)
view_port.add(home_tab)
home_label = Label(home_tab,text='Home').place(x=50,y=50)

finance_tab =ttk.Frame(view_port)
view_port.add(finance_tab)
finance_label = Label(finance_tab,text='Finance').place(x=50,y=50)

inventory_tab =ttk.Frame(view_port)
view_port.add(inventory_tab)
inventory_label = Label(inventory_tab,text='Inventory').place(x=50,y=50)

# SECTION FOR EMPLOYEES
#the section containing frame

employees_tab =ttk.Frame(view_port)
view_port.add(employees_tab)

employees_view_port = ttk.Notebook(employees_tab, width=window_width-150, height=800)
employees_view_port.place(y=-23, x=0)

#Code For EMS Dashboard
employees_dashboard =ttk.Frame(employees_view_port)
employees_view_port.add(employees_dashboard,text='Dashboard')
emp_dashboard_label = Label(employees_dashboard,fg='#c27572',text='EMS Dashboard',font=('Browallia New',50))
emp_dashboard_label.place(x=50,y=10)

#EMS Dashboard Buttons and Elements

#TAB Selection Fucntions

def show_emp_man ():
    employees_view_port.select(employees_management)

def show_ent_man ():
    employees_view_port.select(entity_management)

def show_pay_man ():
    employees_view_port.select(payroll_management)

#EMS DASHBOARD Buttons and There respective labels
emp_man_icon = PhotoImage(file="C:\\Users\\Aramex\\OneDrive\\Pictures\\Saved Pictures\\empman1.png")
emp_management_button = Button(employees_dashboard,image=emp_man_icon,bd=0,text='Manage Employees',relief='flat',command=show_emp_man)
emp_management_button.place(x=240,y=150)
emp_management_label = Label(employees_dashboard,fg='#c27572',bd=0,text='Employees',font=('Browallia New',20))
emp_management_label.place(x=275,y=115)


ent_man_icon = PhotoImage(file="C:\\Users\\Aramex\\OneDrive\\Pictures\\Saved Pictures\\entman1.png")
entity_management_button = Button(employees_dashboard,image=ent_man_icon,bd=0,text='Manage Entities',relief='flat',command=show_ent_man)
entity_management_button.place(x=480,y=150)
ent_management_label = Label(employees_dashboard,fg='#c27572',bd=0,text='Entities',font=('Browallia New',20))
ent_management_label.place(x=535,y=115)

pay_man_icon = PhotoImage(file="C:\\Users\\Aramex\\OneDrive\\Pictures\\Saved Pictures\\payman1.png")
payroll_management_button = Button(employees_dashboard,image=pay_man_icon,bd=0,text='Manage Payrolls',relief='flat',command=show_pay_man)
payroll_management_button.place(x=720,y=150)
pay_management_label = Label(employees_dashboard,fg='#c27572',bd=0,text='Payroll',font=('Browallia New',20))
pay_management_label.place(x=775,y=115)


#EMS DASHBOARD Pages
employees_management =ttk.Frame(employees_view_port)
employees_view_port.add(employees_management,text='Employee Management')

#Employee management elements search box ,add button and table with list

#SEARCH BOX ENTRY FIELD AND SEACH BUTTON
employee_search = Entry(employees_management,width=70,bg='#c27572',fg='white',border=0,font=('Dubai',11))
employee_search.place(y=50,x=300)
employee_search.insert(0,'Enter Employee name or Employee Number')
employee_search.bind("<FocusIn>", lambda e: on_entry_focus(e, employee_search, 'Enter Employee name or Employee Number'))
employee_search.bind("<FocusOut>", lambda e: on_entry_blur(e, employee_search, 'Enter Employee name or Employee Number'))

employee_search_button =Button(employees_management,width=8,bg='#c27572',relief='flat',fg='white',height=1,text='Search')
employee_search_button.place(y=51,x=796)

#Tree to show Employees as table
employees_tree = ttk.Treeview(employees_management,columns=('Employee ID','Full Name','Last Name','Position','Department','Company'),show='headings')
employees_tree.place(y=100,x=50)
employees_tree.heading("#1", text="Employee ID")
employees_tree.heading("#2", text="First Name")
employees_tree.heading("#3", text="Last Name")
employees_tree.heading("#4", text="Position")
employees_tree.heading("#5", text="Department")
employees_tree.heading("#6", text="Company")

employees_tree.column("#1", width=100)
employees_tree.column("#2", width=150)
employees_tree.column("#3", width=150)
employees_tree.column("#4", width=200)
employees_tree.column("#5", width=200)
employees_tree.column("#6", width=250)

#retrieve Employ data and send to tree view

employees_tree.delete(*employees_tree.get_children())

database_view = employee_database("localhost","tulio","MACTulio95","employeedatabase")
emp_info = database_view.retrieve_data(columns=['id','firstname', 'lastname', 'jobposition','department','company'])
database_view.close()

for row in emp_info:
    employees_tree.insert('', 'end', values=row)

#Adding an Employee Buttoon and Data Entry Window
#Add Employee Information Function and Create New Window for data entry
def add_new_employee():
    new_employee_window = tk.Toplevel(main_window)
    new_employee_window.title("Add New Employee")
    new_employee_window.geometry("640x650")
    #new_employee_window.config(bg="#F3D6D5")

    global enddate
    global startdate
    global birthday
########################################################################################################################
    #New Employee Entity Details Form
    entity_details_frame = Frame(new_employee_window, width=300, height=200,relief='groove',bd=2)
    entity_details_frame.place(x=10, y=20)
    entity_details_label = Label(new_employee_window,text='PART A : Entity Details ')
    entity_details_label.place(x=15,y=10)
    #Drop down Menu's
    country_options = ["-Select-","Malawi"]
    district_options = ["-Select-","Blantyre", "Lilongwe", "Mulanje", "Zomba", "Thyolo"]
    company_options = ["-Select-","Yalio Poultry", "Yalio Technologies", "Yalio Transport", "Yalio Retail"]
    department_options = ["-Select-","Accounts and Finance", "Human Resource", "Operations", "Sales and Marketing"]

    country_var = tk.StringVar()
    district_var = tk.StringVar()
    company_var = tk.StringVar()
    department_var= tk.StringVar()

    country_var.set(country_options[0])
    district_var.set(district_options[0])
    company_var.set(company_options[0])
    department_var.set(department_options[0])

    country_label =Label(entity_details_frame,text='Country : ')
    country_label.place(x=5,y= 30)
    country_dropdown = ttk.OptionMenu(entity_details_frame, country_var, *country_options,direction='flush')
    country_dropdown.place(x=80, y=30)

    district_label = Label(entity_details_frame, text='District :')
    district_label.place(x=5, y=70)
    district_dropdown = ttk.OptionMenu(entity_details_frame,district_var,*district_options,direction="flush")
    district_dropdown.place(x=80,y=70)

    company_label = Label(entity_details_frame, text='Company :')
    company_label.place(x=5, y=110)
    company_dropdown = ttk.OptionMenu(entity_details_frame, company_var, *company_options, direction="flush")
    company_dropdown.place(x=80, y=110)

    department_label = Label(entity_details_frame, text='Department :')
    department_label.place(x=5, y=150)
    department_dropdown = ttk.OptionMenu(entity_details_frame, department_var, *department_options, direction="flush")
    department_dropdown.place(x=80, y=150)
#######################################################################################################################

########################################################################################################################
    # New Employee Personal Details Form
    personal_details_frame = Frame(new_employee_window, width=300, height=250, relief='groove', bd=2)
    personal_details_frame.place(x=10, y=240)
    personal_details_label = Label(new_employee_window, text='PART B : Personal details ')
    personal_details_label.place(x=15, y=230)

    firstname_label = Label(personal_details_frame,text='First Name : ')
    firstname_label.place(x=5,y=10)
    firstname_entry = Entry(personal_details_frame,width=30,border=0)
    firstname_entry.place(x=100,y=10)

    middlename_label = Label(personal_details_frame, text='Middle Name : ')
    middlename_label.place(x=5, y=40)
    middlename_entry = Entry(personal_details_frame, width=30,border=0)
    middlename_entry.place(x=100, y=40)

    lastname_label = Label(personal_details_frame, text='Last Name : ')
    lastname_label.place(x=5, y=70)
    lastname_entry = Entry(personal_details_frame, width=30, border=0)
    lastname_entry.place(x=100, y=70)

    #Date of birth data by 3 dropdown menus
    # Define the options for the day, month, and year drop-down menus
    days = list(range(1, 32))
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    years = list(range(1900, 2100))

    # Create the day, month, and year drop-down menus
    dateofbirth_label = tk.Label(personal_details_frame,text='Date of Birth : ')
    dateofbirth_label.place(x=5, y=120)
    day_label = tk.Label(personal_details_frame, text="Day ")
    day_label.place(x=100, y=100)
    day_menu1 = ttk.Combobox(personal_details_frame, values=days,width=2)
    day_menu1.current(0)
    day_menu1.place(x=102, y=120)

    month_label = tk.Label(personal_details_frame, text="Month ")
    month_label.place(x=140, y=100)
    month_menu1 = ttk.Combobox(personal_details_frame, values=months,width=10)
    month_menu1.current(0)
    month_menu1.place(x=142, y=120)

    year_label = tk.Label(personal_details_frame, text="Year ")
    year_label.place(x=230, y=100)
    year_menu1 = ttk.Combobox(personal_details_frame, values=years,width=4)
    year_menu1.current(len(years) - 1)
    year_menu1.place(x=232, y=120)


    #Gender Drop down Menu
    gender = ['Male','Female']
    gender_label = tk.Label(personal_details_frame,text='Sex : ')
    gender_label.place(x=5, y= 160)
    gender_menu = ttk.Combobox(personal_details_frame,values=gender,width=10)
    gender_menu.place(x=100,y =160)

    #Marital Status drop down Menu
    marital_status = ['Single','Married','Divorced','Widowed','Separated']
    marital_status_label = tk.Label(personal_details_frame,text ='Marital Status : ')
    marital_status_label.place(x=5,y = 190)
    marital_status_menu = ttk.Combobox(personal_details_frame,values=marital_status,width=10)
    marital_status_menu.place(x=100, y=190)

    id_number_label = Label(personal_details_frame, text='ID Number : ')
    id_number_label.place(x=5, y=220)
    id_number_entry = Entry(personal_details_frame, width=30, border=0)
    id_number_entry.place(x=100, y=220)
#######################################################################################################################

#######################################################################################################################
    # New Employee Contact Details Form
    contact_details_frame = Frame(new_employee_window, width=300, height=120, relief='groove', bd=2)
    contact_details_frame.place(x=10, y=510)
    contact_details_label = Label(new_employee_window, text='PART C : Contact details ')
    contact_details_label.place(x=15, y=500)

    def validate_phone_number(phone_number):
        pattern = re.compile(r'^\d{10}$')  # phone number should consist of exactly 10 digits
        return bool(pattern.match(phone_number))


    phoneone_label = Label(contact_details_frame, text='Mobile Phone 1 : ')
    phoneone_label.place(x=5, y=10)
    phoneone_entry = Entry(contact_details_frame, width=30, border=0)
    phoneone_entry.place(x=100, y=10)

    phonetwo_label = Label(contact_details_frame, text='Mobile Phone 2 : ')
    phonetwo_label.place(x=5, y=40)
    phonetwo_entry = Entry(contact_details_frame, width=30, border=0)
    phonetwo_entry.place(x=100, y=40)

    def run_code1(event):
        if not validate_phone_number(phoneone_entry.get()):
            notification_bar(new_employee_window, 'Please enter a valid 10-digit phone number', 'bad')
            phoneone_entry.focus()

    phoneone_entry.bind("<FocusOut>",run_code1)



    email_label = Label(contact_details_frame, text='Email address : ')
    email_label.place(x=5, y=70)
    email_entry = Entry(contact_details_frame, width=30, border=0)
    email_entry.place(x=100, y=70)

    physical_address_label = Label(contact_details_frame, text='Physical address : ')
    physical_address_label.place(x=5, y=95)
    physical_address_entry = Entry(contact_details_frame, width=30, border=0)
    physical_address_entry.place(x=100, y=95)

    # New Employee Beneficiary details
    beneficiary_details_frame = Frame(new_employee_window, width=290, height=200, relief='groove',bd=2)
    beneficiary_details_frame.place(x=335, y=20)
    beneficiary_details_label = Label(new_employee_window, text='PART D : Beneficiary Details ')
    beneficiary_details_label.place(x=340, y=10)

    spouse_name_label = Label(beneficiary_details_frame, text='Spouse Name : ')
    spouse_name_label.place(x=5, y=10)
    spouse_name_entry = Entry(beneficiary_details_frame, width=25, border=0)
    spouse_name_entry.place(x=100, y=10)

    spouse_contact_label = Label(beneficiary_details_frame, text='Spouse Contact : ')
    spouse_contact_label.place(x=5, y=40)
    spouse_contact_entry = Entry(beneficiary_details_frame, width=25, border=0)
    spouse_contact_entry.place(x=100, y=40)

    minor_beneficiary_label = Label(beneficiary_details_frame,text="Childens and other Beneficiaires : " )
    minor_beneficiary_label.place(x=5,y=70)
    beneficiary_details_text = Text(beneficiary_details_frame,width=30,height=5)
    beneficiary_details_text.place(x=10 , y=100)
    beneficiary_details_text.insert('1.0','Name of First Beneficiary\nRelationship\nPhone number')

    #Contract Details Form frame
    contract_details_frame = Frame(new_employee_window, width=290, height=220, relief='groove', bd=2)
    contract_details_frame.place(x=335, y=240)
    contract_details_label = Label(new_employee_window, text='PART E : Contract Details ')
    contract_details_label.place(x=340, y=230)

    position_title = ['Ground Manual Worker', 'Irrigation Technician', 'Animal Caretaker', 'Tractor Operator', 'Field Supervisor', 'Farm Manager', 'Marketing Specialist', 'Accountant', 'Human Resources Coordinator', 'Operations Director', 'Administration Officer']
    position_title_label = tk.Label(contract_details_frame, text='Job Position : ')
    position_title_label.place(x=5, y=10)
    position_menu= ttk.Combobox(contract_details_frame, values=position_title, width=25)
    position_menu.place(x=100, y=10)

    contract_type = ['Fixed-Term','Full Time','Internship']
    contract_type_label = tk.Label(contract_details_frame, text='Contract Type : ')
    contract_type_label.place(x=5, y=40)
    contract_type_menu = ttk.Combobox(contract_details_frame, values=contract_type, width=25)
    contract_type_menu.place(x=100, y=40)

    #contract period date picker
    #START DATE
    start_date = Label(contract_details_frame,text='Start Date: ')
    start_date.place(x=5,y=93)
    day_label = tk.Label(contract_details_frame, text="Day ")
    day_label.place(x=100, y=70)
    day_menu2 = ttk.Combobox(contract_details_frame, values=days, width=2)
    day_menu2.current(0)
    day_menu2.place(x=102, y=90)

    month_label = tk.Label(contract_details_frame, text="Month ")
    month_label.place(x=140, y=70)
    month_menu2 = ttk.Combobox(contract_details_frame, values=months, width=10)
    month_menu2.current(0)
    month_menu2.place(x=142, y=90)

    year_label = tk.Label(contract_details_frame, text="Year ")
    year_label.place(x=230, y=70)
    year_menu2 = ttk.Combobox(contract_details_frame, values=years, width=4)
    year_menu2.current(len(years) - 1)
    year_menu2.place(x=232, y=90)

    #END DATE
    end_date = Label(contract_details_frame, text='End Date: ')
    end_date.place(x=5, y=143)
    day_label = tk.Label(contract_details_frame, text="Day ")
    day_label.place(x=100, y=120)
    day_menu3 = ttk.Combobox(contract_details_frame, values=days, width=2)
    day_menu3.current(0)
    day_menu3.place(x=102, y=140)

    month_label = tk.Label(contract_details_frame, text="Month ")
    month_label.place(x=140, y=120)
    month_menu3 = ttk.Combobox(contract_details_frame, values=months, width=10)
    month_menu3.current(0)
    month_menu3.place(x=142, y=140)

    year_label = tk.Label(contract_details_frame, text="Year ")
    year_label.place(x=230, y=120)
    year_menu3 = ttk.Combobox(contract_details_frame, values=years, width=4)
    year_menu3.current(len(years) - 1)
    year_menu3.place(x=232, y=140)

########################################################################################################################
    # Define event listener function for comboboxes
    def update_date(*args):
        #birthday = "{}-{}-{}".format(day_menu1.get(), month_menu1.get(), year_menu1.get())
        startdate = "{}-{}-{}".format(day_menu2.get(), month_menu2.get(), year_menu2.get())
        enddate = "{}-{}-{}".format(day_menu3.get(), month_menu3.get(), year_menu3.get())
        print(startdate, enddate,birthday)  # for testing

    # Add event listeners to comboboxes
    day_menu1.bind("<<ComboboxSelected>>", update_date)
    month_menu1.bind("<<ComboboxSelected>>", update_date)
    year_menu1.bind("<<ComboboxSelected>>", update_date)
    day_menu2.bind("<<ComboboxSelected>>", update_date)
    month_menu2.bind("<<ComboboxSelected>>", update_date)
    year_menu2.bind("<<ComboboxSelected>>", update_date)
    day_menu3.bind("<<ComboboxSelected>>", update_date)
    month_menu3.bind("<<ComboboxSelected>>", update_date)
    year_menu3.bind("<<ComboboxSelected>>", update_date)
########################################################################################################################
    #REMEMBER TO INCLUDE CODE FOR CALCULATING CONTRACT PERIOD
    contract_period = Label(contract_details_frame,text='Contract Period : ')
    contract_period.place(x=5,y=180)
########################################################################################################################

    #PAYROLL Details Frame
    payroll_details_frame = Frame(new_employee_window, width=290, height=120, relief='groove', bd=2)
    payroll_details_frame.place(x=335, y=480)
    contact_details_label = Label(new_employee_window, text='PART F : Payroll details ')
    contact_details_label.place(x=340, y=470)

    basic_pay_label = Label(payroll_details_frame, text='Basic Pay : ')
    basic_pay_label.place(x=5, y=10)
    basic_pay_entry = Entry(payroll_details_frame, width=25, border=0)
    basic_pay_entry.place(x=100, y=10)

    hourly_rate_label = Label(payroll_details_frame, text='Hourly Rate : ')
    hourly_rate_label.place(x=5, y=35)
    hourly_rate_entry = Entry(payroll_details_frame, width=25, border=0)
    hourly_rate_entry.place(x=100, y=35)

    overtime_rate_label = Label(payroll_details_frame, text='Overtime Hourly Rate : ')
    overtime_rate_label.place(x=5, y=65)
    overtime_rate_entry = Entry(payroll_details_frame, width=25, border=0)
    overtime_rate_entry.place(x=100, y=65)

    bank_account_label = Label(payroll_details_frame, text='Bank Account : ')
    bank_account_label.place(x=5, y=90)
    bank_account_entry = Entry(payroll_details_frame, width=15, border=0)
    bank_account_entry.place(x=100, y=90)

    banks = ['National Bank','Standard Bank','FDH Bank','First Capital Bank','NBS Bank Plc','MyBucks Banking Corporation']
    bank_menu = ttk.Combobox(payroll_details_frame, values=banks, width=12)
    bank_menu.current(0)
    bank_menu.place(x=190, y=90)

    give_access = StringVar()
    system_access_check = ttk.Checkbutton(new_employee_window, text='Recommend for System access ', variable=give_access,onvalue='metric', offvalue='imperial')
    system_access_check.place(x=340,y=605)

    def save_employee():
        firstname = firstname_entry.get()
        middlename = middlename_entry.get()
        lastname = lastname_entry.get()
        gender = gender_menu.get()
        maritalstatus = marital_status_menu.get()
        natidnumber = id_number_entry.get()
        country = country_var.get()
        district = district_var.get()
        company = company_var.get()
        department = department_var.get()
        mobilephone1 = phoneone_entry.get()
        mobilephone2 = phonetwo_entry.get()
        emailaddress = email_entry.get()
        physicaladdress = physical_address_entry.get()
        spousename = spouse_name_entry.get()
        spousecontact = spouse_contact_entry.get()
        children = beneficiary_details_text.get('1.0','end')
        jobposition = position_menu.get()
        contracttype = contract_type_menu.get()
        basicpay = basic_pay_entry.get()
        hourlyrate = hourly_rate_entry.get()
        overtime = overtime_rate_entry.get()
        bankaccount = bank_account_entry.get()
        bank = bank_menu.get()

        data = {
            "firstname": firstname,
            "middlename": middlename,
            "lastname": lastname,
            #"dateofbirth":birthday,
            "gender": gender,
            "maritalstatus": maritalstatus,
            "natidnumber": natidnumber,
            "country": country,
            "district": district,
            "company": company,
            "department": department,
            "mobilephone1": mobilephone1,
            "mobilephone2": mobilephone2,
            "emailaddress": emailaddress,
            "physicaladdress": physicaladdress,
            "spousename": spousename,
            "spousecontact": spousecontact,
            "children": children,
            "jobposition": jobposition,
            "contracttype": contracttype,
            "startdate": startdate,
            "enddate": enddate,
            "basicpay": basicpay,
            "hourlyrate": hourlyrate,
            "overtime": overtime,
            "bankaccount": bankaccount,
            "bank": bank
                    }
        employee_db = employee_database("localhost","tulio","MACTulio95","employeedatabase")
        employee_db.add_employee(data)
        employee_db.commit()
        employee_db.close()

        employees_tree.delete(*employees_tree.get_children())

        database_view = employee_database("localhost", "tulio", "MACTulio95", "employeedatabase")
        emp_info = database_view.retrieve_data(
            columns=['id', 'firstname', 'lastname', 'jobposition', 'department', 'company'])
        database_view.close()

        for row in emp_info:
            employees_tree.insert('', 'end', values=row)

        notification_bar(new_employee_window,"Employee added Successfully!",'bad')
        new_employee_window.after(1500, new_employee_window.withdraw)



    save_button =Button(new_employee_window,text='Save',width=10,height=1,font=('Dubai',10),background='#1E8449',command=save_employee)
    save_button.place(x=540,y=605)


#Add Employee Button
add_emp_icon = PhotoImage(file="C:\\Users\\Aramex\\OneDrive\\Pictures\\Saved Pictures\\addemp11.png")
add_employee_button =Button(employees_management,image=add_emp_icon,bd=0,command=add_new_employee)
add_employee_button.place(y=10,x=1000)


entity_management =ttk.Frame(employees_view_port)
employees_view_port.add(entity_management,text='Entity Management')
entity_management_label = Label(entity_management,text='Entity Management').place(x=50,y=50)


payroll_management =ttk.Frame(employees_view_port)
employees_view_port.add(payroll_management,text='Payroll Management')
payroll_management_label = Label(payroll_management,text='Payroll Management').place(x=50,y=50)


#Customers Tab
customers_tab = ttk.Frame(view_port)
view_port.add(customers_tab)
customers_label = Label(customers_tab,text='Customers').place(x=50,y=50)

reports_tab =ttk.Frame(view_port)
view_port.add(reports_tab)
reports_label = Label(reports_tab,text='Reports').place(x=50,y=50)

settings_tab = ttk.Frame(view_port)
view_port.add(settings_tab)
settings_label = Label(settings_tab,text='Settings').place(x=50,y=50)


#Creating information bar
info_bar = Frame(main_window,width=window_width-150,height=33,bg='#343131')
info_bar.place(y=0,x=150)

#Code For Info bar text label and placement
info_bar_text = Label(info_bar,text='Section label ',bd=0,bg='#343131',fg='white',font=('Browallia New',15))
info_bar_text.place(y=7,x=500)


#code to be replaced with code that pulls out username and displays on information Bar
username_container = ('User : ' + 'Macdonald Juma')
username_label_info = Label(info_bar,text=username_container,bg='#343131',fg='white')
username_label_info.place(y=10,x=1020)

#profile image resizing and placing on information Bar

#load image Here
profile_pic = Image.open("C:\\Users\\Aramex\\OneDrive\\Pictures\\Saved Pictures\\profile.jpg")

# Resize the image to the desired size
profile_pic = profile_pic.resize((33, 33), Image.LANCZOS)

# Convert the image to a PhotoImage object for Tkinter
profile_pic = ImageTk.PhotoImage(profile_pic)

# Create a label to display the image
profile_label = Label(info_bar, image=profile_pic)
profile_label.place(y=0,x=1160)




main_window.mainloop()