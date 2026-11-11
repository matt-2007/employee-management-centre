import random
import tkinter as tk
from tkinter import *
import time
import tkinter.ttk as ttk
import tkinter.filedialog
import os
import sys
import sqlite3
import calendar
from tkcalendar import DateEntry  # type: ignore

class EICOuter:
    def __init__(ELM): #Setting window attributes
        ELM.window = tk.Tk()
        ELM.window.title("Data Collection Page")
        ELM.window.geometry("900x1080")  #sets window size
        ELM.window.attributes('-fullscreen', False)
        ELM.window.configure(bg = "#efefef") #sets window background colour
        ELM.frame = Frame(ELM.window) #Sets a frame within the window
        ELM.frame.pack(side="top", expand=True, fill="both")
       
       
        def Outer():

            def CreateLeaveRequest():
                for ELM.widgets in ELM.frame.winfo_children(): #Clears the frame
                    ELM.widgets.destroy()

                def Retry():
                    for ELM.widgets in ELM.frame.winfo_children(): #Clears the frame
                        ELM.widgets.destroy()
                    CreateLeaveRequest()

                def finish():
                    ELM.LeaveStartSelected = ELM.LeaveStartDate.get() #.gets of the user entry
                    ELM.LeaveEndSelected = ELM.LeaveEndDate.get()

                    ELM.DataEntries = [ELM.LeaveID, ELM.EmployeeID, ELM.Firstname, ELM.Surname, ELM.LeaveType, ELM.Reason] #Stores the entries by the user into the array
                    k = -1

                    for i in ELM.DataEntries: #Loops through the array
                            k = k + 1 #Increments by one
                            i = i.get() #Sets i to the .get of the value it is currently on in the array
                            if i.isdigit() == True:
                                i = int(i) #Turns string i into int i
                                ELM.DataEntries[k] = i #Stores new value for i in the array
                            else:
                                ELM.DataEntries[k] = i #Stores new value for i in the array


                    ELM.DataEntryAccept = True
                    while ELM.DataEntryAccept == True:
                        for index, val in enumerate(ELM.DataEntries):
                            if isinstance(ELM.DataEntries[index], int) == True: #If the value in array is int then passes
                                pass
                            elif len(ELM.DataEntries[index]) == 0: #If not int then checks length, if 0 it gives error
                                ELM.PresenceCheckFail = tk.Label(ELM.frame, text="This cannot be empty").grid(row=index, column=3)
                                ELM.DataEntryAccept = False #Stops data entry
                        break
                    if ELM.DataEntryAccept == False:
                        ELM.RetryButton = tk.Button(ELM.frame, text="Retry", command = Retry).grid(row=14, column=1) #Creates retry button
                           
                    ELM.LeaveStatus = "Pending"
                   
                    if ELM.DataEntryAccept == True: #Inserts data into the leave table
                        try:
                            sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                            cursor = sqliteConnection.cursor()
                            cursor.execute("INSERT INTO EmployeeLeave (leaveid, employeeid, firstname, surname, leavetype, reason, leavestart, leaveend, status) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (ELM.DataEntries[0], ELM.DataEntries[1], ELM.DataEntries[2], ELM.DataEntries[3], ELM.DataEntries[4], ELM.DataEntries[5], ELM.LeaveStartSelected, ELM.LeaveEndSelected, ELM.LeaveStatus))
                            sqliteConnection.commit()
                            cursor.close()
                            print("Data stored successfully")
                            CreateLeaveRequest()
                        except sqlite3.Error as error:
                            print("Error occured - ", error)



                def ReturnToSelection(): #Goes back to main menu
                    for ELM.widgets in ELM.frame.winfo_children():
                        ELM.widgets.destroy()
                    Outer()


                   
               
                ELM.LeaveID_entry = tk.Label(ELM.frame, text="Leave ID", font=("Georgia", 20), fg = 'black').grid(row=0) #Labes  for leave
                ELM.EmployeeID_entry = tk.Label(ELM.frame, text="Employee ID", font=("Georgia", 20), fg = 'black').grid(row=1)
                ELM.FirstName_entry = tk.Label(ELM.frame, text="Firstname", font=("Georgia", 20), fg = 'black').grid(row=2)
                ELM.Surname_entry = tk.Label(ELM.frame, text="Surname", font=("Georgia", 20), fg = 'black').grid(row=3)
                ELM.LeaveType_entry = tk.Label(ELM.frame, text="Leave Type", font=("Georgia", 20), fg = 'black').grid(row=4)
                ELM.Reason_entry = tk.Label(ELM.frame, text="Reason", font=("Georgia", 20), fg = 'black').grid(row=5)
                ELM.LeaveStart_entry = tk.Label(ELM.frame, text="Leave Start", font=("Georgia", 20), fg = 'black').grid(row=6)
                ELM.LeaveEnd_entry = tk.Label(ELM.frame, text="Leave End", font=("Georgia", 20), fg = 'black').grid(row=7)

               
                ELM.Finish_button = tk.Button(ELM.frame, text="Finish", command=finish).grid(row=12, column=1, sticky=tk.W, pady=4) #Creates buttons
                ELM.Return_button = tk.Button(ELM.frame, text="Return to selection", command=ReturnToSelection).grid(row=13, column=1, sticky=tk.W, pady=4)
               
                ELM.LeaveID = tk.Entry(ELM.frame) #Entry boxes for leave
                ELM.EmployeeID = tk.Entry(ELM.frame)
                ELM.Firstname = tk.Entry(ELM.frame)
                ELM.Surname = tk.Entry(ELM.frame)
                ELM.LeaveType = StringVar()
                ELM.Reason = tk.Entry(ELM.frame)
                ELM.LeaveStartDate = DateEntry(ELM.frame, date_pattern="dd-mm-yyyy") #Calender widgets for leave
                ELM.LeaveEndDate = DateEntry(ELM.frame, date_pattern="dd-mm-yyyy")

                                 
                ELM.LeaveTypeChosen = ttk.Combobox(ELM.frame, width = 17, textvariable = ELM.LeaveType, state='readonly') #Combobox for leave (dropdown)
                ELM.LeaveTypeChosen['values'] = ("Annual Leave", "Sick Leave", "Maternity Leave", "Paternity Leave")
                ELM.LeaveTypeChosen.current(0) #Starting value for it is values[0] = annual leave
                ELM.LeaveTypeChosen.grid(row=4, column=1)

                ELM.LeaveID.grid(row=0, column=1) #places the entry boxes
                ELM.EmployeeID.grid(row=1, column=1)
                ELM.Firstname.grid(row=2, column=1)
                ELM.Surname.grid(row=3, column=1)
                ELM.Reason.grid(row=5, column=1)
                ELM.LeaveStartDate.grid(row=6, column=1)
                ELM.LeaveEndDate.grid(row=7, column=1)





            def ViewLeaveRequests():
                for ELM.widgets in ELM.frame.winfo_children(): #Clears frame
                    ELM.widgets.destroy()
                try:
                    sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                    cursor = sqliteConnection.cursor()
                    cursor.execute("SELECT * FROM EmployeeLeave WHERE status = 'Pending'"); #Selects all rows where status is pending
                    row = cursor.fetchall()
                    sqliteConnection.commit()
                    cursor.close()
                except sqlite3.Error as error:
                    print("Error occured - ", error) #Prints error to console if there is one
               
                def ReSearch():
                    ViewLeaveRequests() #Used when searching for 2nd, 3rd, 4th time and so on

           

                def ApproveLeave(): #Defines how leave is approved
                    try:
                        sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                        cursor = sqliteConnection.cursor()
                        cursor.execute("SELECT * FROM EmployeeLeave WHERE status = 'Pending'");
                        row = cursor.fetchall()
                        sqliteConnection.commit()
                        cursor.close()
                    except sqlite3.Error as error:
                        print("Error occured - ", error)
                    ELM.LeaveID = row[ELM.PCE][0] #Defines as corresponding position in 2d array
                    ELM.EmployeeID = row[ELM.PCE][1]
                    ELM.Firstname = row[ELM.PCE][2]
                    ELM.Surname = row[ELM.PCE][3]
                    ELM.LeaveType = row[ELM.PCE][4]
                    ELM.Reason = row[ELM.PCE][5]
                    ELM.LeaveStartSelected = row[ELM.PCE][6]
                    ELM.LeaveEndSelected = row[ELM.PCE][7]
                    ELM.LeaveStatus = row[ELM.PCE][8]
                    ELM.LeaveAccept = "Accepted" #Makes leaveaccept accepted, used when inputting back into database
                    try: #Inputs new LeaveAccept value into database
                        sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                        cursor = sqliteConnection.cursor()
                        cursor.execute("INSERT INTO employeeleave (leaveid, employeeid, firstname, surname, leavetype, reason, leavestart, leaveend, status) VALUES(?,?,?,?,?,?,?,?,?) ON CONFLICT (leaveid) DO UPDATE SET status = ? WHERE leaveid = ?", (ELM.LeaveID, ELM.EmployeeID, ELM.Firstname, ELM.Surname, ELM.LeaveType, ELM.Reason, ELM.LeaveStartSelected, ELM.LeaveEndSelected, ELM.LeaveStatus, ELM.LeaveAccept, ELM.LeaveID));
                        row = cursor.fetchall()
                        sqliteConnection.commit()
                        cursor.close()
                    except sqlite3.Error as error:
                        print("Error occured - ", error)

                def DenyLeave(): #Defines how leave is denied
                    try:
                        sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                        cursor = sqliteConnection.cursor()
                        cursor.execute("SELECT * FROM EmployeeLeave WHERE status = 'Pending'");
                        row = cursor.fetchall()
                        sqliteConnection.commit()
                        cursor.close()
                    except sqlite3.Error as error:
                        print("Error occured - ", error)
                    ELM.LeaveID = row[ELM.PCE][0] #Defines as corresponding position in 2d array
                    ELM.EmployeeID = row[ELM.PCE][1]
                    ELM.Firstname = row[ELM.PCE][2]
                    ELM.Surname = row[ELM.PCE][3]
                    ELM.LeaveType = row[ELM.PCE][4]
                    ELM.Reason = row[ELM.PCE][5]
                    ELM.LeaveStartSelected = row[ELM.PCE][6]
                    ELM.LeaveEndSelected = row[ELM.PCE][7]
                    ELM.LeaveStatus = row[ELM.PCE][8]
                    ELM.LeaveDeny = "Denied" #Makes leavedeny denied, used when inputting back into database
                    try:
                        sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                        cursor = sqliteConnection.cursor()
                        cursor.execute("INSERT INTO employeeleave (leaveid, employeeid, firstname, surname, leavetype, reason, leavestart, leaveend, status) VALUES(?,?,?,?,?,?,?,?,?) ON CONFLICT (leaveid) DO UPDATE SET status = ? WHERE leaveid = ?", (ELM.LeaveID, ELM.EmployeeID, ELM.Firstname, ELM.Surname, ELM.LeaveType, ELM.Reason, ELM.LeaveStartSelected, ELM.LeaveEndSelected, ELM.LeaveStatus, ELM.LeaveDeny, ELM.LeaveID));
                        row = cursor.fetchall()
                        sqliteConnection.commit()
                        cursor.close()
                    except sqlite3.Error as error:
                        print("Error occured - ", error)

                def PendingEntry():

                    ELM.PCE = 0



                    ELM.PendingLeaveIDLabel = tk.Label(ELM.frame, text="Leave ID", font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=3, column=0) #labels for displaying data
                    ELM.PendingEmployeeIDLabel = tk.Label(ELM.frame, text="Employee ID", font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=4, column=0)
                    ELM.PendingFirstnameLabel = tk.Label(ELM.frame, text="Firstname", font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=5, column=0)
                    ELM.PendingSurnameLabel = tk.Label(ELM.frame, text="Surname", font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=6, column=0)
                    ELM.PendingLeaveTypeLabel = tk.Label(ELM.frame, text="Leave Type", font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=7, column=0)
                    ELM.PendingReasonLabel = tk.Label(ELM.frame, text="Reason", font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=8, column=0)
                    ELM.PendingLeaveStartLabel = tk.Label(ELM.frame, text="Leave Start", font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=9, column=0)
                    ELM.PendingLeaveEndLabel = tk.Label(ELM.frame, text="Leave End", font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=10, column=0)
                    ELM.PendingStatusLabel = tk.Label(ELM.frame, text="Status", font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=11, column=0)

                    ELM.PendingLeaveID = tk.Label(ELM.frame, text=row[ELM.PCE][0], font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=3, column=1) #Labels containing the variable data
                    ELM.PendingEmployeeID = tk.Label(ELM.frame, text=row[ELM.PCE][1], font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=4, column=1)
                    ELM.PendingFirstname = tk.Label(ELM.frame, text=row[ELM.PCE][2], font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=5, column=1)
                    ELM.PendingSurname = tk.Label(ELM.frame, text=row[ELM.PCE][3], font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=6, column=1)
                    ELM.PendingLeaveType = tk.Label(ELM.frame, text=row[ELM.PCE][4], font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=7, column=1)
                    ELM.PendingReason = tk.Label(ELM.frame, text=row[ELM.PCE][5], font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=8, column=1)
                    ELM.PendingLeaveStart = tk.Label(ELM.frame, text=row[ELM.PCE][6], font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=9, column=1)
                    ELM.PendingLeaveEnd = tk.Label(ELM.frame, text=row[ELM.PCE][7], font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=10, column=1)
                    ELM.PendingStatus = tk.Label(ELM.frame, text=row[ELM.PCE][8], font=("Arial", 15), width=15, borderwidth=2, relief="solid").grid(row=11, column=1)

                    ELM.EmptySpace2 = tk.Label(ELM.frame, font=("Georgia", 15),fg='black',width=15).grid(row=12, column=0) #Empty placeholder

                    ELM.ReSearchButton = tk.Button(ELM.frame, text="Retry", command=ReSearch).grid(row=13, column=0) #Buttons to search, approve and deny
                    ELM.ApproveButton = tk.Button(ELM.frame, text="Approve", command=ApproveLeave).grid(row=13, column=1)
                    ELM.DenyButton = tk.Button(ELM.frame, text="Deny", command=DenyLeave).grid(row=13, column=2)
 
                   


                ELM.PendingRequests = len(row)
                ELM.PendingRequestsTemp = str(ELM.PendingRequests)

                ELM.PendingRequestLabel = tk.Label(ELM.frame, text=ELM.PendingRequestsTemp + " Pending Requests", font=("Arial", 15)).grid(row=0, column=0)
                ELM.EmptySpace1 = tk.Label(ELM.frame, font=("Georgia", 15),fg='black',width=15).grid(row=0, column=1)

                ELM.PendingEntryButton = tk.Button(ELM.frame, text="Confirm", command=PendingEntry).grid(row=2, column=0)




            ELM.TitleDisplay_label = tk.Label(ELM.frame, text="Employee Leave Management",font=("Arial", 30))
            ELM.TitleDisplay_label.place(x=175, y=50)
           
           
            ELM.CreateLeaveButton = tk.Button(ELM.frame, text='Make Leave Request', command=CreateLeaveRequest, font=("Georgia", 20), bg ='#999999', fg = 'black', height=2, width=20)
            ELM.CreateLeaveButton.place(x=300, y=175)

            ELM.ViewLeaveButton = tk.Button(ELM.frame, text='View Leave Requests', command=ViewLeaveRequests, font=("Georgia", 20), bg='#999999', fg = 'black', height = 2, width=20)
            ELM.ViewLeaveButton.place(x=300, y=300)
       
        Outer()
    def run(ELM):
        ELM.window.mainloop()

ELM = EICOuter()
ELM.run()
