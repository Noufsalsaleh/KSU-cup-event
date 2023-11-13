from tkinter import *
import sqlite3
import tkinter as tk
from tkinter import messagebox
import re
from random import randint
from tkinter import ttk

conn = sqlite3.connect('KSUCup.db')

c = conn.cursor()
c.execute(''' Create table IF NOT EXISTS stu(
StuID      Char(10) Primary Key    ,
FName     CHAR (30)    ,
LName     CHAR (30)    ,
Password        CHAR (30)  ,
Email         CHAR (30)    ,
mobileNo  CHAR(15)
 ); ''')

c.execute(''' Create table IF NOT EXISTS sportEvent(
eventID    Char(5) Primary Key ,
eventName  CHAR (30),
eventLoc   CHAR (30),
eventCap INT,
reservDate  Date,
reservTime CHAR(5)
); ''')

c.execute(''' Create table IF NOT EXISTS reservation(
reservID Char(5) Primary Key,
StuID      CHAR(10),
eventID      CHAR(10) ,
FOREIGN KEY(StuID) REFERENCES stu(StuID) ,
FOREIGN KEY(eventID) REFERENCES sportEvent(eventID) 
 ); ''')
print("--------------------------  stusednt info ---------------")
c.execute("Select * from stu")
print(c.fetchall())
print("--------------------------  sportEvent info ---------------")
c.execute("Select * from sportEvent")
print(c.fetchall())
print("--------------------------  reservation info ---------------")
c.execute("Select * from reservation")
print(c.fetchall())
conn.close()  #########
# login
userid1 = ""


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x200')
        self.root.title("KSU Event Reservation System")
        self.userVar = tk.StringVar()
        self.passwordVar = tk.StringVar()
        self.idLabel = tk.Label(self.root, text="ID :", width=20, font=("bold", 10))
        self.idLabel.place(x=0, y=60)
        self.idEntry = tk.Entry(self.root, textvariable=self.userVar)
        self.idEntry.place(x=170, y=60)

        self.usrLabel = tk.Label(self.root, text="Password :", width=20, font=("bold", 10))
        self.usrLabel.place(x=0, y=90)
        self.userEntry = tk.Entry(self.root, textvariable=self.passwordVar, show='*')
        self.userEntry.place(x=170, y=90)
        login = tk.Button(self.root, text="Sign in", width=10, command=self.signin)
        login.place(x=120, y=130)
        signup = tk.Button(self.root, text="Sign up", width=10, command=self.signup)
        signup.place(x=220, y=130)
        self.root.mainloop()

    def signup(self):
        print("hello")
        # Create window of sign up
        self.root = tk.Tk()
        self.root.geometry('400x350')
        self.root.title("Student Registration")

        # Signup label
        self.label21 = tk.Label(self.root, text="Student Registration", width=25, bg="AntiqueWhite3", font=("bold", 22))
        self.label21.place(x=0, y=0)
        # StudentID label
        self.label24 = tk.Label(self.root, text="StudentID:", bg="AntiqueWhite3", width=17, font=("bold", 10))
        self.label24.place(x=50, y=80)
        self.entry_3 = tk.Entry(self.root)
        self.entry_3.place(x=200, y=80)
        # First name label
        self.label22 = tk.Label(self.root, text="First Name:", bg="AntiqueWhite3", width=17, font=("bold", 10))
        self.label22.place(x=50, y=110)
        self.fNameEntry = tk.Entry(self.root)
        self.fNameEntry.place(x=200, y=110)
        # Last name label
        self.label23 = tk.Label(self.root, text="Last Name", bg="AntiqueWhite3", width=17, font=("bold", 10))
        self.label23.place(x=50, y=140)
        self.lNameEntry = tk.Entry(self.root)
        self.lNameEntry.place(x=200, y=140)
        # Password label
        self.label24 = tk.Label(self.root, text="Password:", bg="AntiqueWhite3", width=17, font=("bold", 10))
        self.label24.place(x=50, y=170)
        self.passEntry = tk.Entry(self.root)
        self.passEntry.place(x=200, y=170)
        # Email label
        self.label25 = tk.Label(self.root, text="Email address:", bg="AntiqueWhite3", width=17, font=("bold", 10))
        self.label25.place(x=50, y=200)
        self.emailEntry = tk.Entry(self.root)
        self.emailEntry.place(x=200, y=200)
        # Phone number label
        self.label26 = tk.Label(self.root, text="Phone number:", bg="AntiqueWhite3", width=17, font=("bold", 10))
        self.label26.place(x=50, y=230)
        self.mobileEntry = tk.Entry(self.root)
        self.mobileEntry.place(x=200, y=230)
        # Submit button
        self.SubmetButton = tk.Button(self.root, text='save', width=20, bg='AntiqueWhite3', fg='black',
                                      command=self.saveStuInf).place(x=120, y=280)

        print("Student registration window  seccussfully created.....")

        self.root.mainloop()

    def saveStuInf(self):
        try:
            conn = sqlite3.connect('KSUCup.db')
            c = conn.cursor()
            # student id
            StuID = str(self.entry_3.get())
            reg = "^[0-9]{10}$"
            x = re.search(re.compile(reg), StuID)
            # validate StuID
            if not x:
                messagebox.showinfo("Invalid student ID", "Student ID must be consists of 10 digits")
                return
            # first &last Name
            firstname = str(self.fNameEntry.get())
            lastname = str(self.lNameEntry.get())
            if not firstname or not lastname:
                messagebox.showinfo("missing input", "first name and last name should not be empty")
                return
            # validate password
            password = str(self.passEntry.get())
            reg = "^[A-Za-z0-9]{6,100}$"
            pat = re.compile(reg)
            x = re.search(pat, password)
            if not x:
                password = ''
                messagebox.showinfo("invalid password format",
                                    "password must consists at least of 6 digits or letters")
                return

            # validate phone
            mobile = str(self.mobileEntry.get())
            reg2 = "^(05)[0-9]{8}$"
            y = re.search(re.compile(reg2), mobile)
            if not y:
                messagebox.showinfo("Invalid Mobile Number",
                                    "Mobile Number must be consists of 10 digits and starts with \'05\'")
                return
            # validate email
            email = str(self.emailEntry.get())
            reg = "^([a-zA-Z0-9\._-]+){8}(@ksu\.edu\.sa)$"
            z = re.search(re.compile(reg), email)
            if not z:
                messagebox.showinfo("invalid Email", "Email should be in formate of xxxxxxxx@ksu.edu.sa ")
                return
            # insert and check if id is exist
            id = c.execute(f"SELECT StuID FROM stu WHERE StuID = {StuID}")
            if len(id.fetchall()) == 0:
                sql = """INSERT INTO stu VALUES('{}','{}','{}','{}','{}','{}')
                """.format(StuID, firstname, lastname, password, email, mobile)
                c.execute(sql)
                conn.commit()
                messagebox.showinfo("Registration Done", "Congratulation You information has been saved")
                self.root.destroy()
            else:
                messagebox.showinfo("ID already exist", "The enterd id is exist pleas try with another ID")
            conn.close()
        except sqlite3.Error:
            messagebox.showinfo("database error", "DataBase ERROR")

        except:
            messagebox.showinfo("error", "something wrong happend and record not saved")

    # admin window to add events
    def addEventsWindow(self):
        self.root = tk.Tk()
        self.root.geometry('400x350')
        self.root.title("Register New Sport Event")

        # form event label
        self.label31 = tk.Label(self.root, text="Register New Sport Event", width=25, bg="AntiqueWhite3",
                                font=("bold", 22))
        self.label31.place(x=0, y=0)

        self.label32 = tk.Label(self.root, text="Event Name:", bg="AntiqueWhite3",
                                width=17, font=("bold", 10))
        self.label32.place(x=50, y=80)
        self.eventNameEntry = tk.Entry(self.root)
        self.eventNameEntry.place(x=200, y=80)
        # eventLocation
        self.label32 = tk.Label(self.root, text="Event Location:",
                                bg="AntiqueWhite3", width=17, font=("bold", 10))
        self.label32.place(x=50, y=110)
        self.eventLocEntry = tk.Entry(self.root)
        self.eventLocEntry.place(x=200, y=110)
        # event Cap
        self.label35 = tk.Label(self.root, text="Event Capcity:",
                                bg="AntiqueWhite3", width=17, font=("bold", 10))
        self.label35.place(x=50, y=140)
        self.eventCapEntry = tk.Entry(self.root)
        self.eventCapEntry.place(x=200, y=140)
        # eventDate
        self.label33 = tk.Label(self.root, text="Event Date:",
                                bg="AntiqueWhite3", width=17, font=("bold", 10))
        self.label33.place(x=50, y=170)
        self.eventDateEntry = tk.Entry(self.root)
        self.eventDateEntry.place(x=200, y=170)
        # eventTime
        self.label33 = tk.Label(self.root, text="Event Time:",
                                bg="AntiqueWhite3", width=17, font=("bold", 10))
        self.label33.place(x=50, y=200)
        self.eventTimeEntry = tk.Entry(self.root)
        self.eventTimeEntry.place(x=200, y=200)

        # Submit button
        self.SubmetButton = tk.Button(self.root, text='save', width=10, bg='AntiqueWhite3', fg='black',
                                      command=self.addEventsToDB).place(x=100, y=230)
        # Submit button
        self.LogoutButton = tk.Button(self.root, text='Logout', width=10, bg='AntiqueWhite3', fg='black',
                                      command=self.logout).place(x=200, y=230)

        print("Admin window seccussfully created.....")

        self.root.mainloop()

    def addEventsToDB(self):
        try:
            conn = sqlite3.connect('KSUCup.db')
            c = conn.cursor()
            # event id
            evID = str(randint(10000, 99999))  # generate random number of 5 digit

            # eventName
            eventName = str(self.eventNameEntry.get())
            if not eventName:
                messagebox.showinfo("missing input", "Event name should not be empty")
                return
            # eventLoc
            eventLoc = str(self.eventLocEntry.get())
            if not eventLoc:
                messagebox.showinfo("missing input", "Event Location should not be empty")
                return
            # eventDate
            EvDate = str(self.eventDateEntry.get())
            #vlidate date
            reg = "^(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9])/[0-9]{4}$"
            x = re.search(re.compile(reg), EvDate)
            if not x:
                messagebox.showinfo("invalid Date format",
                                    "Entred date must be dd/mm/yyyy")
                return
            # eventTime
            eventTime = str(self.eventTimeEntry.get())
            #validate time
            reg = "^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"
            x = re.search(re.compile(reg), eventTime)
            if not x:
                messagebox.showinfo("invalid Time format",
                                    "Entred Time must be in form of hh:MM")
                return
            # tickit Capcity
            eventCap = str(self.eventCapEntry.get())
            if not eventCap:
                messagebox.showinfo("missing input", "Event capacity should not be empty")
                return
            reg = "^[0-9]*$"
            x = re.search(re.compile(reg), eventCap)

            if not x:
                messagebox.showinfo("Invalid input", "Event capacity must be digits")
                return

            # insert and check if id is exist
            id = c.execute(f"SELECT eventID FROM sportEvent WHERE eventID = {evID}")
            if len(id.fetchall()) == 0:
                sql = """INSERT INTO sportEvent VALUES('{}','{}','{}','{}','{}','{}')
                """.format(evID, eventName, eventLoc, eventCap, EvDate, eventTime)
                c.execute(sql)
                conn.commit()
                messagebox.showinfo("New Sport Event Added", "New Sport Event has been registered")
                # self.eventName.delete(0,END)
                self.eventDateEntry.delete(0, END)
                self.eventNameEntry.delete(0, END)
                self.eventLocEntry.delete(0, END)
                self.eventCapEntry.delete(0, END)
                self.eventTimeEntry.delete(0, END)

            else:
                messagebox.showinfo("ID already exist", "The enterd id is exist pleas try with another ID")
            conn.close()
        except sqlite3.Error:
            messagebox.showinfo("database error", "DataBase ERROR")

        except:
            messagebox.showinfo("error", "something wrong happend and record not saved")

    # ------------------------- Booking Tickits --------------------------------
    def bookingTickitsWindow(self, uid):
        self.root = tk.Tk()
        self.root.geometry('700x400')
        self.root.title("Booking Tickits")

        # create a notebook
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        # create frames
        self.frame1 = ttk.Frame(self.notebook, width=500, height=200)
        self.frame2 = ttk.Frame(self.notebook, width=500, height=200)

        # add frames to notebook

        self.notebook.add(self.frame1, text='Book a Ticket')
        self.notebook.add(self.frame2, text='View my tickets')

        # tab1
        #book an event
        conn = sqlite3.connect('KSUCup.db')
        self.tv = ttk.Treeview(self.frame1, columns=(1, 2, 3, 4, 5, 6), show='headings', height=8)

        self.tv.heading(1, text="Event ID")
        self.tv.column(1, minwidth=20, width=60, anchor=CENTER, stretch=NO)
        self.tv.heading(2, text="Event Name")
        self.tv.column(2, minwidth=20, width=150, anchor=CENTER, stretch=NO)
        self.tv.heading(3, text="Event Loc")
        self.tv.column(3, minwidth=20, width=150, anchor=CENTER, stretch=NO)
        self.tv.heading(4, text="Event capcity")
        self.tv.column(4, minwidth=20, width=100, anchor=CENTER, stretch=NO)
        self.tv.heading(5, text="Event Date")
        self.tv.column(5, minwidth=20, width=80, anchor=CENTER, stretch=NO)
        self.tv.heading(6, text="Event Time")
        self.tv.column(6, minwidth=20, width=60, anchor=CENTER, stretch=NO)

        # tab2
        #view my tickets
        self.tv2 = ttk.Treeview(self.frame2, columns=(1, 2, 3, 4, 5), show='headings', height=8)

        self.tv2.heading(1, text="Event ID")
        self.tv2.column(1, minwidth=20, width=60, anchor=CENTER, stretch=NO)
        self.tv2.heading(2, text="Event Name")
        self.tv2.column(2, minwidth=20, width=200, anchor=CENTER, stretch=NO)
        self.tv2.heading(3, text="Event Loc")
        self.tv2.column(3, minwidth=20, width=200, anchor=CENTER, stretch=NO)
        self.tv2.heading(4, text="Event Date")
        self.tv2.column(4, minwidth=20, width=80, anchor=CENTER, stretch=NO)
        self.tv2.heading(5, text="Event Time")
        self.tv2.column(5, minwidth=20, width=60, anchor=CENTER, stretch=NO)

        self.tv2.pack()

        cursor = conn.execute("SELECT * from sportEvent")
        count = 0
        for row in cursor:
            self.tv.insert(parent='', index=count, text='', values=(row[0], row[1], row[2], row[3],
            row[4], row[5]))
            count += 1

        print("Operation done successfully")

        self.tv.pack()

        self.uid1 = uid
        self.SubmetButton = ttk.Button(self.frame1, text='Book', width=20, command=self.bookDB)
        self.SubmetButton.pack(side="bottom")

        self.LogoutButton = ttk.Button(self.frame1, text='Logout', width=20, command=self.logout)
        self.LogoutButton.pack(side="bottom")

        self.SubmetButton2 = ttk.Button(self.frame2, text='show', width=20, command=self.tabRefresh)
        self.SubmetButton2.pack(side="bottom")

        self.LogoutButton3 = ttk.Button(self.frame2, text='Logout', width=20, command=self.logout)
        self.LogoutButton3.pack(side="bottom")

        conn.close()

        print("Admin window seccussfully created.....")

        self.root.mainloop()

    def tabRefresh(self):
        tabNo = str(self.notebook.index(self.notebook.select()))
        if tabNo == "1":
            for item in self.tv2.get_children():
                self.tv2.delete(item)
            conn = sqlite3.connect('KSUCup.db')
            cursor = conn.execute(
                f"SELECT  reservation.eventID,eventName,eventLoc,reservDate,reservTime from stu,sportEvent,reservation where stu.StuID=reservation.StuID and sportEvent.eventID=reservation.eventID and reservation.StuID= {self.uid1}")
            count = 0
            for row in cursor:
                self.tv2.insert(parent='', index=count, text='', values=(row[0], row[1], row[2], row[3], row[4]))
                count += 1
            self.tv2.pack()
            conn.close()
        return

    def bookDB(self):
        try:
            conn = sqlite3.connect('KSUCup.db')
            c = conn.cursor()
            # event id & userid
            selectedItem = self.tv.selection()[0]
            evID = str(self.tv.item(selectedItem)['values'][0])

            reservID = str(randint(10000, 99999))  # generate random number of 5 digit

            # insert and check if id is exist
            id = c.execute(
                f"SELECT  reservation.eventID,eventName,eventLoc,reservDate,reservTime from stu,sportEvent,reservation where stu.StuID=reservation.StuID and sportEvent.eventID=reservation.eventID and reservation.StuID= {self.uid1} and reservation.eventID={evID}")
            if len(id.fetchall()) == 0:
                id = c.execute(f"SELECT eventCap from  sportEvent where eventID = {evID} and eventCap != 0")
                if len(id.fetchall()) == 0:
                    messagebox.showinfo("Book faild", "No more Booking Available")
                else:
                    sql = """INSERT INTO reservation VALUES('{}','{}','{}')
                    """.format(reservID, self.uid1, evID)
                    c.execute(sql)
                    c.execute(f"UPDATE sportEvent set eventCap = eventCap-1 where  eventID={evID}")
                    conn.commit()
                    messagebox.showinfo("Booking Succeed", "Your booking has been registered")

            else:
                messagebox.showinfo("Booking Fail", "this event already booked")
                conn.close()
        except sqlite3.Error:
            messagebox.showinfo("database error", "DataBase ERROR")

        except:
            messagebox.showinfo("error", "something wrong happend and record not saved")

    # ---------------------------
    # singin methode
    def signin(self):
        if len(self.userVar.get()) == 0 or len(self.passwordVar.get()) == 0:
            messagebox.showinfo("Error", "Pleas Enter ID and Password")
        else:
            reg = "^[0-9]{10}$"
            x = re.search(re.compile(reg), str(self.userVar.get()))
            if not x and self.userVar.get() != "admin":
                messagebox.showinfo("Invalid ID", "ID number must be consists of 10 digits")
                self.userVar.set("")
                self.passwordVar.set("")
                return
            conn = sqlite3.connect('KSUCup.db')
            c = conn.cursor()
            c.execute('SELECT * FROM stu WHERE StuID = ? and Password = ?', (self.idEntry.get(), self.userEntry.get()))
            check = c.fetchone()
            if check == None:
                if self.userVar.get() == "admin" and self.passwordVar.get() == "111111":
                    self.root.destroy()
                    self.addEventsWindow()
                    print("admin")
                else:
                    messagebox.showinfo("Error", "Invalid ID or password ")
                    self.userVar.set("")
                    self.passwordVar.set("")
            else:

                try:
                    self.root.destroy()
                except:
                    pass

                self.bookingTickitsWindow(self.userVar.get())

            conn.close()

    def logout(self):
        self.root.destroy()
        self.__init__()


gui = GUI()