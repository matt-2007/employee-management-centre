import random
from tkinter import *
import tkinter as tk
import time
from tkinter.ttk import *
import tkinter.filedialog
import os
import sys
import sqlite3
from tkcalendar import DateEntry # type: ignore

class EICOuter: #Sets the attributes of the window
    def __init__(EmInCo):
        EmInCo.window = tk.Tk()
        EmInCo.window.title("Data Collection Page")
        EmInCo.window.geometry("900x1080")  #sets window size
        EmInCo.window.attributes('-fullscreen', False)
        EmInCo.window.configure(bg = "#efefef") #sets window background colour
        EmInCo.frame = Frame(EmInCo.window) #Sets a frame within the window
        EmInCo.frame.pack(side="top", expand=True, fill="both")
       
       

        def Outer():
            def ReturnToSelection(): #Used to go back to the main menu
                for EmInCo.widgets in EmInCo.frame.winfo_children():
                    EmInCo.widgets.destroy()
                Outer()

            def AddNewEmployee(): #Overarching function for the entirety of creating a new employee
                for EmInCo.widgets in EmInCo.frame.winfo_children(): #Clears all widgets in frame
                    EmInCo.widgets.destroy()

                EmInCo.DataEntryAccept = True



                def finish(): # Clears frame and calls it again
                    def retry():
                        for EmInCo.widgets in EmInCo.frame.winfo_children(): #Clears the frame
                            EmInCo.widgets.destroy()
                        AddNewEmployee() #Calls the frame again with nothing on it

                    def retrybutton(): # Creates a button to retry with
                        EmInCo.Retry_button = tk.Button(EmInCo.frame, text="Retry", command=retry).grid(row=12, column=2, sticky=tk.W, pady=4) #Upon entering a string that does not contain solely numbers, retry button appears

                    EmInCo.EmployeeFirstName = EmInCo.FirstName.get() #Gets the values held in each of the corresponding variables, only .get can be used with SQL
                    EmInCo.EmployeeSurname = EmInCo.Surname.get()  
                    EmInCo.EmployeeGender = EmInCo.Gender.get()
                    EmInCo.EmployeeStatus = EmInCo.Status.get()
                    EmInCo.EmployeeTitle = EmInCo.JobTitle.get()
                    EmInCo.EmployeePhoneNo = EmInCo.PhoneNumber.get()
                    EmInCo.EmployeeEmail = EmInCo.Email.get()

                    EmInCo.PresenceCheck = True
                    while EmInCo.PresenceCheck == True: # Checks to make sure there are not empty fields and that FirstName and Surname are of correct length
                        if len(EmInCo.EmployeeFirstName) > 15:
                            EmInCo.EFN_ErrorBox = tk.Label(EmInCo.frame, text="15 Characters max", font=("Georgia", 20), fg = 'black').grid(row=1, column=2)
                            EmInCo.PresenceCheck = False
                            EmInCo.DataEntryAccept = False
                        if EmInCo.EmployeeFirstName == "":
                            EmInCo.EFN_ErrorBox = tk.Label(EmInCo.frame, text="This cannot be blank", font=("Georgia", 20), fg = 'black').grid(row=1, column=2)
                            EmInCo.PresenceCheck = False
                            EmInCo.DataEntryAccept = False
                        if len(EmInCo.EmployeeSurname) > 20:
                            EmInCo.ESN_ErrorBox = tk.Label(EmInCo.frame, text="20 Characters max", font=("Georgia", 20), fg = 'black').grid(row=2, column=2)
                            EmInCo.PresenceCheck = False
                            EmInCo.DataEntryAccept = False
                        if EmInCo.EmployeeSurname == "":
                            EmInCo.ESN_Errorbox= tk.Label(EmInCo.frame, text="This cannot be blank", font=("Georgia", 20), fg = 'black').grid(row=2, column=2)                    
                            EmInCo.PresenceCheck = False
                            EmInCo.DataEntryAccept = False
                        if EmInCo.EmployeeGender == "":
                            EmInCo.EG_ErrorBox = tk.Label(EmInCo.frame, text="This cannot be blank", font=("Georgia", 20), fg = 'black').grid(row=4, column=2)
                            EmInCo.PresenceCheck = False
                            EmInCo.DataEntryAccept = False
                        if EmInCo.EmployeeStatus == "":
                            EmInCo.ES_ErrorBox = tk.Label(EmInCo.frame, text="This cannot be blank", font=("Georgia", 20), fg = 'black').grid(row=5, column=2)
                            EmInCo.PresenceCheck = False
                            EmInCo.DataEntryAccept = False
                        if EmInCo.EmployeeTitle == "":
                            EmInCo.ET_ErrorBox = tk.Label(EmInCo.frame, text="This cannot be blank", font=("Georgia", 20), fg = 'black').grid(row=6, column=2)
                            EmInCo.PresenceCheck = False
                            EmInCo.DataEntryAccept = False
                        if EmInCo.EmployeePhoneNo == "":
                            EmInCo.EPN_ErrorBox = tk.Label(EmInCo.frame, text="This cannot be blank", font=("Georgia", 20), fg = 'black').grid(row=8, column=2)
                            EmInCo.PresenceCheck = False
                            EmInCo.DataEntryAccept = False
                        if EmInCo.EmployeeEmail == "":
                            EmInCo.EE_ErrorBox = tk.Label(EmInCo.frame, text="This cannot be blank", font=("Georgia", 20), fg = 'black').grid(row=7, column=2)
                            EmInCo.PresenceCheck = False
                            EmInCo.DataEntryAccept = False
                        break
                    if EmInCo.PresenceCheck == False: #If any validation failed, the retry button appears
                        retrybutton()

                    try:
                        EmInCo.EmployeeIDTemp = EmInCo.EmployeeID.get() #Takes the value of EmployeeID and stores it as a variable (.get cannot be converted to int)
                        EmInCo.EmployeeIDInt = int(EmInCo.EmployeeIDTemp) #Converts the variable into an integer    
                    except:
                        EmInCo.DataEntryAccept = False
                        EmInCo.ErrorBox1 = tk.Label(EmInCo.frame, text="You must enter a number for the EmployeeID", font=("Georgia", 20), fg = 'black').grid(row=0, column=2) #Creates error boxex
                        retrybutton()

                    try:
                        EmInCo.EmployeeAgeTemp = EmInCo.Age.get() #Tries to convert from string to int, if it can't it assumes you entered something other than a string and it creates an error box
                        EmInCo.EmployeeAgeInt = int(EmInCo.EmployeeAgeTemp)
                    except:
                        EmInCo.DataEntryAccept = False
                        EmInCo.ErrorBox2 = tk.Label(EmInCo.frame, text="You must enter a number for the age",font=("Georgia", 20), fg = 'black').grid(row=3, column=2)
                        retrybutton()

                    try:
                        EmInCo.EmployeeSalaryTemp = EmInCo.Salary.get()
                        EmInCo.EmployeeSalaryFloat = float(EmInCo.EmployeeSalaryTemp)
                    except:
                        EmInCo.DataEntryAccept = False
                        EmInCo.ErrorBox3 = tk.Label(EmInCo.frame, text="You must enter a value for salary (No symbols)", font=("Georgia", 20), fg= 'black').grid(row=9, column=2)


                    if EmInCo.DataEntryAccept == True: #This inserts the data given by the user into the database only if condition is true and there are no errors
                        try:
       
                            sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                            cursor = sqliteConnection.cursor()

                            cursor.execute("INSERT INTO EmployeeInformation (employeeid, firstname, surname, age, gender, status, jobtitle, phonenumber, email, salary) VALUES(?,?,?,?,?,?,?,?,?,?)", (EmInCo.EmployeeIDInt, EmInCo.EmployeeFirstName, EmInCo.EmployeeSurname, EmInCo.EmployeeAgeInt, EmInCo.EmployeeGender, EmInCo.EmployeeStatus, EmInCo.EmployeeTitle, EmInCo.EmployeePhoneNo, EmInCo.EmployeeEmail, EmInCo.EmployeeSalaryFloat));

                            sqliteConnection.commit()
                   
                            cursor.close()

                            print("Data stored successfully")

                            AddNewEmployee()
                        except sqlite3.Error as error:
                            print('Error occurred - ', error)
                            EmInCo.ErrorBox4 = tk.Label(EmInCo.frame, text="Employee ID already in use", font=("Georgia", 20), fg='black').grid(row=14, column=2) #Error incase the username is already taken
                        finally:
                            if sqliteConnection:
                                sqliteConnection.close()
                    else:
                        EmInCo.ErrorBox5 = tk.Label(EmInCo.frame, text="This entry has not been stored", font=("Georgia", 20), fg='black').grid(row=13, column=2)

                       

                EmInCo.EmployeeID_entry = tk.Label(EmInCo.frame, text="Employee ID Number", font=("Georgia", 20), fg = 'black').grid(row=0) #Creates the UI labels
                EmInCo.FirstName_entry = tk.Label(EmInCo.frame, text="First Name", font=("Georgia", 20), fg = 'black').grid(row=1)
                EmInCo.Surname_entry = tk.Label(EmInCo.frame, text="Surname", font=("Georgia", 20), fg = 'black').grid(row=2)
                EmInCo.Age_entry = tk.Label(EmInCo.frame, text="Age", font=("Georgia", 20), fg = 'black').grid(row=3)
                EmInCo.Gender_entry = tk.Label(EmInCo.frame, text="Gender", font=("Georgia", 20), fg = 'black').grid(row=4)
                EmInCo.Status_entry = tk.Label(EmInCo.frame, text="Status", font=("Georgia", 20), fg = 'black').grid(row=5)
                EmInCo.JobTitle_entry = tk.Label(EmInCo.frame, text="Job Title", font=("Georgia", 20), fg = 'black').grid(row=6)
                EmInCo.Email_entry = tk.Label(EmInCo.frame, text="Email", font=("Georgia", 20), fg = 'black').grid(row=7)
                EmInCo.PhoneNumber_entry = tk.Label(EmInCo.frame, text="Phone Number", font=("Georgia", 20), fg = 'black').grid(row=8)
                EmInCo.Salary_entry = tk.Label(EmInCo.frame, text="Salary", font=("Georgia", 20), fg = 'black').grid(row=9)
               
                EmInCo.Finish_button = tk.Button(EmInCo.frame, text="Finish", command=finish).grid(row=12, column=1, sticky=tk.W, pady=4) #Creates the UI buttons
                EmInCo.Return_button = tk.Button(EmInCo.frame, text="Return to selection", command=ReturnToSelection).grid(row=13, column=1, sticky=tk.W, pady=4)
               
                EmInCo.EmployeeID = tk.Entry(EmInCo.frame) #Creates the UI entry boxes (for text entry)
                EmInCo.FirstName = tk.Entry(EmInCo.frame)
                EmInCo.Surname = tk.Entry(EmInCo.frame)
                EmInCo.Age = tk.Entry(EmInCo.frame)
                EmInCo.Gender = tk.Entry(EmInCo.frame)
                EmInCo.Status = tk.Entry(EmInCo.frame)
                EmInCo.JobTitle = tk.Entry(EmInCo.frame)
                EmInCo.Email = tk.Entry(EmInCo.frame)
                EmInCo.PhoneNumber = tk.Entry(EmInCo.frame)
                EmInCo.Salary = tk.Entry(EmInCo.frame)

                EmInCo.EmployeeID.grid(row=0, column=1) #Places the entry boxes
                EmInCo.FirstName.grid(row=1, column=1)
                EmInCo.Surname.grid(row=2, column=1)
                EmInCo.Age.grid(row=3, column=1)
                EmInCo.Gender.grid(row=4, column=1)
                EmInCo.Status.grid(row=5, column=1)
                EmInCo.JobTitle.grid(row=6, column=1)
                EmInCo.Email.grid(row=7, column=1)
                EmInCo.PhoneNumber.grid(row=8, column=1)
                EmInCo.Salary.grid(row=9, column=1)

               
               
            def SearchAndEdit():
                for EmInCo.widgets in EmInCo.frame.winfo_children(): #Clears frame
                    EmInCo.widgets.destroy()

                def RetrySearch(): #Recalls the function
                    SearchAndEdit()
               
                def SearchDB():
                    EmInCo.SearchButton.destroy()
                    EmInCo.EIDEntry.config(state="disabled") #Stops the entry box being typed in

                    EmInCo.RetrySearchButton = tk.Button(EmInCo.frame, text="Retry", command=RetrySearch)
                    EmInCo.RetrySearchButton.grid(row=1, column=0)
               
                    EmInCo.RetrySearch = tk.Label(EmInCo.frame, text="Retry Search", font=("Georgia", 15),fg="black")
                   
                    try:
                        EmInCo.EIDTemp = EmInCo.EIDEntry.get() #Tries to turn string to int
                        EmInCo.EIDInt = int(EmInCo.EIDTemp)
                    except:
                        EmInCo.SearchErrorbox1 = tk.Label(EmInCo.frame, text="Please enter a number for the employee ID", font=("Georgia", 15),fg='black',width=35, borderwidth=2, relief="solid").grid(column=0,row=5)

                    def FNConfirm(): #Inserts Firstname if appended
                            EmInCo.FNAppendGet = EmInCo.FNAppendEntry.get()
                            try:
                                sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                                cursor = sqliteConnection.cursor()

                                cursor.execute("INSERT INTO employeeinformation (employeeid, firstname, surname, age, gender, status, jobtitle, phonenumber, email, salary) VALUES(?,?,?,?,?,?,?,?,?,?) ON CONFLICT (employeeid) DO UPDATE SET firstname = ? WHERE employeeid = ?", (EmInCo.EIDTemp, EmInCo.FirstNameResult, EmInCo.SurnameResult, EmInCo.AgeResult, EmInCo.GenderResult, EmInCo.StatusResult, EmInCo.JobTitleResult, EmInCo.PhoneNumberResult, EmInCo.EmailResult, EmInCo.SalaryResult, EmInCo.FNAppendGet, EmInCo.EIDTemp));

                                sqliteConnection.commit()
                       
                                cursor.close()
                            except sqlite3.Error as error:
                                print('Error occurred - ', error)
                            finally:
                                if sqliteConnection:
                                    sqliteConnection.close()
                    def SNConfirm(): #Inserts surname if appended
                        EmInCo.SNAppendGet = EmInCo.SNAppendEntry.get()
                        try:
                            sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                            cursor = sqliteConnection.cursor()

                            cursor.execute("INSERT INTO employeeinformation (employeeid, firstname, surname, age, gender, status, jobtitle, phonenumber, email, salary) VALUES(?,?,?,?,?,?,?,?,?,?) ON CONFLICT (employeeid) DO UPDATE SET surname = ? WHERE employeeid = ?", (EmInCo.EIDTemp, EmInCo.FirstNameResult, EmInCo.SurnameResult, EmInCo.AgeResult, EmInCo.GenderResult, EmInCo.StatusResult, EmInCo.JobTitleResult, EmInCo.PhoneNumberResult, EmInCo.EmailResult, EmInCo.SalaryResult, EmInCo.SNAppendGet, EmInCo.EIDTemp));

                            sqliteConnection.commit()
                       
                            cursor.close()
                        except sqlite3.Error as error:
                            print('Error occurred - ', error)
                        finally:
                            if sqliteConnection:
                                sqliteConnection.close()
                    def AgeConfirm(): #Inserts age if appended
                        EmInCo.AgeAppendGet = EmInCo.AgeAppendEntry.get()
                        try:
                            sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                            cursor = sqliteConnection.cursor()

                            cursor.execute("INSERT INTO employeeinformation (employeeid, firstname, surname, age, gender, status, jobtitle, phonenumber, email, salary) VALUES(?,?,?,?,?,?,?,?,?,?) ON CONFLICT (employeeid) DO UPDATE SET age = ? WHERE employeeid = ?", (EmInCo.EIDTemp, EmInCo.FirstNameResult, EmInCo.SurnameResult, EmInCo.AgeResult, EmInCo.GenderResult, EmInCo.StatusResult, EmInCo.JobTitleResult, EmInCo.PhoneNumberResult, EmInCo.EmailResult, EmInCo.SalaryResult, EmInCo.AgeAppendGet, EmInCo.EIDTemp));

                            sqliteConnection.commit()
                       
                            cursor.close()
                        except sqlite3.Error as error:
                            print('Error occurred - ', error)
                        finally:
                            if sqliteConnection:
                                sqliteConnection.close()
                    def GenderConfirm(): #Inserts gender if appended
                        EmInCo.GenderAppendGet = EmInCo.GenderAppendEntry.get()
                        try:
                            sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                            cursor = sqliteConnection.cursor()

                            cursor.execute("INSERT INTO employeeinformation (employeeid, firstname, surname, age, gender, status, jobtitle, phonenumber, email, salary) VALUES(?,?,?,?,?,?,?,?,?,?) ON CONFLICT (employeeid) DO UPDATE SET gender = ? WHERE employeeid = ?", (EmInCo.EIDTemp, EmInCo.FirstNameResult, EmInCo.SurnameResult, EmInCo.AgeResult, EmInCo.GenderResult, EmInCo.StatusResult, EmInCo.JobTitleResult, EmInCo.PhoneNumberResult, EmInCo.EmailResult, EmInCo.SalaryResult, EmInCo.GenderAppendGet, EmInCo.EIDTemp));

                            sqliteConnection.commit()
                       
                            cursor.close()
                        except sqlite3.Error as error:
                            print('Error occurred - ', error)
                        finally:
                            if sqliteConnection:
                                sqliteConnection.close()
                    def StatusConfirm(): #Inserts status if appended
                        EmInCo.StatusAppendGet = EmInCo.StatusAppendEntry.get()
                        try:
                            sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                            cursor = sqliteConnection.cursor()

                            cursor.execute("INSERT INTO employeeinformation (employeeid, firstname, surname, age, gender, status, jobtitle, phonenumber, email, salary) VALUES(?,?,?,?,?,?,?,?,?,?) ON CONFLICT (employeeid) DO UPDATE SET status = ? WHERE employeeid = ?", (EmInCo.EIDTemp, EmInCo.FirstNameResult, EmInCo.SurnameResult, EmInCo.AgeResult, EmInCo.GenderResult, EmInCo.StatusResult, EmInCo.JobTitleResult, EmInCo.PhoneNumberResult, EmInCo.EmailResult, EmInCo.SalaryResult, EmInCo.StatusAppendGet, EmInCo.EIDTemp));

                            sqliteConnection.commit()
                       
                            cursor.close()
                        except sqlite3.Error as error:
                            print('Error occurred - ', error)
                        finally:
                            if sqliteConnection:
                                sqliteConnection.close()
                    def TitleConfirm(): #Inserts title if appended
                        EmInCo.TitleAppendGet = EmInCo.TitleAppendEntry.get()
                        try:
                            sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                            cursor = sqliteConnection.cursor()

                            cursor.execute("INSERT INTO employeeinformation (employeeid, firstname, surname, age, gender, status, jobtitle, phonenumber, email, salary) VALUES(?,?,?,?,?,?,?,?,?,?) ON CONFLICT (employeeid) DO UPDATE SET jobtitle = ? WHERE employeeid = ?", (EmInCo.EIDTemp, EmInCo.FirstNameResult, EmInCo.SurnameResult, EmInCo.AgeResult, EmInCo.GenderResult, EmInCo.StatusResult, EmInCo.JobTitleResult, EmInCo.PhoneNumberResult, EmInCo.EmailResult, EmInCo.SalaryResult, EmInCo.TitleAppendGet, EmInCo.EIDTemp));

                            sqliteConnection.commit()
                       
                            cursor.close()
                        except sqlite3.Error as error:
                            print('Error occurred - ', error)
                        finally:
                            if sqliteConnection:
                                sqliteConnection.close()
                    def NoConfirm(): #Inserts number if appended
                        EmInCo.NoAppendGet = EmInCo.PhoneAppendEntry.get()
                        try:
                            sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                            cursor = sqliteConnection.cursor()

                            cursor.execute("INSERT INTO employeeinformation (employeeid, firstname, surname, age, gender, status, jobtitle, phonenumber, email, salary) VALUES(?,?,?,?,?,?,?,?,?,?) ON CONFLICT (employeeid) DO UPDATE SET phonenumber = ? WHERE employeeid = ?", (EmInCo.EIDTemp, EmInCo.FirstNameResult, EmInCo.SurnameResult, EmInCo.AgeResult, EmInCo.GenderResult, EmInCo.StatusResult, EmInCo.JobTitleResult, EmInCo.PhoneNumberResult, EmInCo.EmailResult, EmInCo.SalaryResult, EmInCo.NoAppendGet, EmInCo.EIDTemp));

                            sqliteConnection.commit()
                       
                            cursor.close()
                        except sqlite3.Error as error:
                            print('Error occurred - ', error)
                        finally:
                            if sqliteConnection:
                                sqliteConnection.close()
                    def EmConfirm(): #Inserts email if appended
                        EmInCo.EmAppendGet = EmInCo.EmailAppendEntry.get()
                        try:
                            sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                            cursor = sqliteConnection.cursor()

                            cursor.execute("INSERT INTO employeeinformation (employeeid, firstname, surname, age, gender, status, jobtitle, phonenumber, email, salary) VALUES(?,?,?,?,?,?,?,?,?,?) ON CONFLICT (employeeid) DO UPDATE SET email = ? WHERE employeeid = ?", (EmInCo.EIDTemp, EmInCo.FirstNameResult, EmInCo.SurnameResult, EmInCo.AgeResult, EmInCo.GenderResult, EmInCo.StatusResult, EmInCo.JobTitleResult, EmInCo.PhoneNumberResult, EmInCo.EmailResult, EmInCo.SalaryResult, EmInCo.EmAppendGet, EmInCo.EIDTemp));

                            sqliteConnection.commit()
                       
                            cursor.close()
                        except sqlite3.Error as error:
                            print('Error occurred - ', error)
                        finally:
                            if sqliteConnection:
                                sqliteConnection.close()
                    def SalConfirm(): #Inserts salary if appended
                        EmInCo.SalAppendGet = EmInCo.SalAppendEntry.get()
                        try:
                            sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                            cursor = sqliteConnection.cursor()

                            cursor.execute("INSERT INTO employeeinformation (employeeid, firstname, surname, age, gender, status, jobtitle, phonenumber, email, salary) VALUES(?,?,?,?,?,?,?,?,?,?) ON CONFLICT (employeeid) DO UPDATE SET salary = ? WHERE employeeid = ?", (EmInCo.EIDTemp, EmInCo.FirstNameResult, EmInCo.SurnameResult, EmInCo.AgeResult, EmInCo.GenderResult, EmInCo.StatusResult, EmInCo.JobTitleResult, EmInCo.PhoneNumberResult, EmInCo.EmailResult, EmInCo.SalaryResult, EmInCo.SalAppendGet, EmInCo.EIDTemp));

                            sqliteConnection.commit()
                       
                            cursor.close()
                        except sqlite3.Error as error:
                            print('Error occurred - ', error)
                        finally:
                            if sqliteConnection:
                                sqliteConnection.close()

                    def FNAppend(): #Creates buttons for appending
                        EmInCo.FNAppendLabel = tk.Label(EmInCo.frame, text="Firstname:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=17)
                        EmInCo.FNAppendEntry = tk.Entry(EmInCo.frame)
                        EmInCo.FNAppendEntry.grid(column=2, row=17)
                        EmInCo.FNAppendConfirm = tk.Button(EmInCo.frame, text="Confirm", command=FNConfirm).grid(column=3, row=17)
                    def SNAppend(): #Creates buttons for appending
                        EmInCo.SNAppendLabel = tk.Label(EmInCo.frame, text="Surname:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=18)
                        EmInCo.SNAppendEntry = tk.Entry(EmInCo.frame)
                        EmInCo.SNAppendEntry.grid(column=2, row=18)
                        EmInCo.SNAppendConfirm = tk.Button(EmInCo.frame, text="Confirm", command=SNConfirm).grid(column=3, row=18)
                    def AgeAppend(): #Creates buttons for appending
                        EmInCo.AgeAppendLabel = tk.Label(EmInCo.frame, text="Age:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=19)
                        EmInCo.AgeAppendEntry = tk.Entry(EmInCo.frame)
                        EmInCo.AgeAppendEntry.grid(column=2, row=19)
                        EmInCo.AgeAppenedConfirm = tk.Button(EmInCo.frame, text="Confirm", command=AgeConfirm).grid(column=3, row=19)
                    def GenderAppend(): #Creates buttons for appending
                        EmInCo.GenderAppendLabel = tk.Label(EmInCo.frame, text="Gender:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=20)
                        EmInCo.GenderAppendEntry = tk.Entry(EmInCo.frame)
                        EmInCo.GenderAppendEntry.grid(column=2, row=20)
                        EmInCo.GenderAppendConfirm = tk.Button(EmInCo.frame, text="Confirm", command=GenderConfirm).grid(column=3, row=20)
                    def StatusAppend(): #Creates buttons for appending
                        EmInCo.StatusAppendLabel = tk.Label(EmInCo.frame, text="Status:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=21)
                        EmInCo.StatusAppendEntry = tk.Entry(EmInCo.frame)
                        EmInCo.StatusAppendEntry.grid(column=2, row=21)
                        EmInCo.StatusAppendConfirm = tk.Button(EmInCo.frame, text="Confirm", command=StatusConfirm).grid(column=3, row=21)
                    def TitleAppend(): #Creates buttons for appending
                        EmInCo.TitleAppendLabel = tk.Label(EmInCo.frame, text="Job Title:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=22)
                        EmInCo.TitleAppendEntry = tk.Entry(EmInCo.frame)
                        EmInCo.TitleAppendEntry.grid(column=2, row=22)
                        EmInCo.TitleAppendConfirm = tk.Button(EmInCo.frame, text="Confirm",command=TitleConfirm).grid(column=3, row=22)
                    def NoAppend(): #Creates buttons for appending
                        EmInCo.PhoneAppendLabel = tk.Label(EmInCo.frame, text="Phone Number:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=23)
                        EmInCo.PhoneAppendEntry = tk.Entry(EmInCo.frame)
                        EmInCo.PhoneAppendEntry.grid(column=2, row=23)
                        EmInCo.NoAppendConfirm = tk.Button(EmInCo.frame, text="Confirm", command=NoConfirm).grid(column=3, row=23)
                    def EmAppend(): #Creates buttons for appending
                        EmInCo.EmailAppendLabel = tk.Label(EmInCo.frame, text="Email Address:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=24)
                        EmInCo.EmailAppendEntry = tk.Entry(EmInCo.frame)
                        EmInCo.EmailAppendEntry.grid(column=2, row=24)
                        EmInCo.EmAppendConfirm = tk.Button(EmInCo.frame, text="Confirm",command=EmConfirm).grid(column=3, row=24)
                    def SalAppend(): #Creates buttons for appending
                        EmInCo.SalAppendLabel = tk.Label(EmInCo.frame, text="Salary:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=25)
                        EmInCo.SalAppendEntry = tk.Entry(EmInCo.frame)
                        EmInCo.SalAppendEntry.grid(column=2, row=25)
                        EmInCo.SalAppendConfirm = tk.Button(EmInCo.frame, text="Confirm", command=SalConfirm).grid(column=3, row=25)



                    try: #Used to search the database, searches for records with employeeid = input
                            sqliteConnection = sqlite3.connect('EmployeeManagementCenter.db')
                            cursor = sqliteConnection.cursor()

                            cursor.execute("SELECT * FROM EmployeeInformation WHERE employeeid = ?", (EmInCo.EIDTemp));
                            row = cursor.fetchone()

                            sqliteConnection.commit()
                   
                            cursor.close()
                    except sqlite3.Error as error:
                        print('Error occurred - ', error)
                    finally:
                        if sqliteConnection:
                            sqliteConnection.close()

                    try: #Stores the results from the SQL SELECT query into these variables to be accessed later
                        EmInCo.EmployeeIDResult = row[0]        
                        EmInCo.FirstNameResult = row[1]
                        EmInCo.SurnameResult = row[2]
                        EmInCo.AgeResult = row[3]
                        EmInCo.GenderResult = row[4]
                        EmInCo.StatusResult = row[5]
                        EmInCo.JobTitleResult = row[6]
                        EmInCo.PhoneNumberResult = row[7]
                        EmInCo.EmailResult = row[8]
                        EmInCo.SalaryResult = row[9]



                        EmInCo.EmployeeIDLabel = tk.Label(EmInCo.frame, text="Employee ID:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=3) #Creates labels
                        EmInCo.FirstNameLabel = tk.Label(EmInCo.frame, text="Firstname:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=4)
                        EmInCo.SurnameLabel = tk.Label(EmInCo.frame, text="Surname:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=5)
                        EmInCo.AgeLabel = tk.Label(EmInCo.frame, text="Age:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=6)
                        EmInCo.GenderLabel = tk.Label(EmInCo.frame, text="Gender:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=7)
                        EmInCo.StatusLabel = tk.Label(EmInCo.frame, text="Status:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=8)
                        EmInCo.JobTitleLabel = tk.Label(EmInCo.frame, text="Job Title:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=9)
                        EmInCo.EmailLabel = tk.Label(EmInCo.frame, text="Email Address:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=10)
                        EmInCo.PhoneNumberLabel = tk.Label(EmInCo.frame, text="Phone Number:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=11)
                        EmInCo.SalaryLabel = tk.Label(EmInCo.frame, text="Salary:", font=("Georgia", 15),fg='black',width=15, borderwidth=2, relief="solid").grid(column=0,row=12)

                        EmInCo.EmptySpace1 = tk.Label(EmInCo.frame, font=("Georgia", 15),fg='black',width=15).grid(column=0,row=13) #Creates empty labels to serve as placeholders
                        EmInCo.EmptySpace2 = tk.Label(EmInCo.frame, font=("Georgia", 15),fg='black',width=15).grid(column=0,row=14)
                        EmInCo.EmptySpace3 = tk.Label(EmInCo.frame, font=("Georgia", 15),fg='black',width=15).grid(column=0,row=15)
                        EmInCo.EmptySpace4 = tk.Label(EmInCo.frame, font=("Georgia", 15),fg='black',width=15).grid(column=0,row=16)

                        EmInCo.EmptySpace5 = tk.Label(EmInCo.frame, font=("Georgia", 15),fg='black',width=15).grid(column=2,row=13)
                        EmInCo.EmptySpace6 = tk.Label(EmInCo.frame, font=("Georgia", 15),fg='black',width=15).grid(column=2,row=14)
                        EmInCo.EmptySpace7 = tk.Label(EmInCo.frame, font=("Georgia", 15),fg='black',width=15).grid(column=2,row=15)
                        EmInCo.EmptySpace8 = tk.Label(EmInCo.frame, font=("Georgia", 15),fg='black',width=15).grid(column=2,row=16)
                       



                        EmInCo.EmployeeIDDisplay = tk.Label(EmInCo.frame, text=EmInCo.EmployeeIDResult, font=("Georgia", 15),fg='black',width=30, borderwidth=2, relief="solid").grid(column=2,row=3) #Creates labels
                        EmInCo.FirstNameDisplay = tk.Label(EmInCo.frame, text=EmInCo.FirstNameResult, font=("Georgia", 15),fg='black',width=30, borderwidth=2, relief="solid").grid(column=2,row=4)
                        EmInCo.SurnameDisplay = tk.Label(EmInCo.frame, text=EmInCo.SurnameResult, font=("Georgia", 15),fg='black',width=30, borderwidth=2, relief="solid").grid(column=2,row=5)
                        EmInCo.AgeDisplay = tk.Label(EmInCo.frame, text=EmInCo.AgeResult, font=("Georgia", 15),fg='black',width=30, borderwidth=2, relief="solid").grid(column=2,row=6)
                        EmInCo.GenderDisplay = tk.Label(EmInCo.frame, text=EmInCo.GenderResult, font=("Georgia", 15),fg='black',width=30, borderwidth=2, relief="solid").grid(column=2,row=7)
                        EmInCo.StatusDisplay = tk.Label(EmInCo.frame, text=EmInCo.StatusResult, font=("Georgia", 15),fg='black',width=30, borderwidth=2, relief="solid").grid(column=2,row=8)
                        EmInCo.JobTitleDisplay = tk.Label(EmInCo.frame, text=EmInCo.JobTitleResult, font=("Georgia", 15),fg='black',width=30, borderwidth=2, relief="solid").grid(column=2,row=9)
                        EmInCo.EmailDisplay = tk.Label(EmInCo.frame, text=EmInCo.EmailResult, font=("Georgia", 15),fg='black',width=30, borderwidth=2, relief="solid").grid(column=2,row=10)
                        EmInCo.PhoneNumberDisplay = tk.Label(EmInCo.frame, text=EmInCo.PhoneNumberResult, font=("Georgia", 15),fg='black',width=30, borderwidth=2, relief="solid").grid(column=2,row=11)
                        EmInCo.SalaryDisplay = tk.Label(EmInCo.frame, text="£"+str(EmInCo.SalaryResult), font=("Georgia", 15),fg='black',width=30, borderwidth=2, relief="solid").grid(column=2,row=12)

                        EmInCo.FNAppendButton = tk.Button(EmInCo.frame, text="Append", command=FNAppend).grid(column=4, row=4) #Creates buttons
                        EmInCo.SNAppendButton = tk.Button(EmInCo.frame, text="Append", command=SNAppend).grid(column=4, row=5)
                        EmInCo.AgeAppendButton = tk.Button(EmInCo.frame, text="Append", command=AgeAppend).grid(column=4, row=6)
                        EmInCo.GenderAppendButton = tk.Button(EmInCo.frame, text="Append", command=GenderAppend).grid(column=4, row=7)
                        EmInCo.StatusAppendButton = tk.Button(EmInCo.frame, text="Append", command=StatusAppend).grid(column=4, row=8)
                        EmInCo.TitleAppendButton = tk.Button(EmInCo.frame, text="Append", command=TitleAppend).grid(column=4, row=9)
                        EmInCo.EmAppendButton = tk.Button(EmInCo.frame, text="Append", command=EmAppend).grid(column=4, row=10)
                        EmInCo.NoAppendButton = tk.Button(EmInCo.frame, text="Append", command=NoAppend).grid(column=4, row=11)
                        EmInCo.SalAppendButton = tk.Button(EmInCo.frame, text="Append", command=SalAppend).grid(column=4, row=12)

                    except:
                        EmInCo.SearchErrorbox2 = tk.Label(EmInCo.frame, text="This employee ID cannot be found", font=("Georgia", 15),fg='black',width=35, borderwidth=2, relief="solid").grid(column=0,row=7) #Error if employee id entered cannot be found
               
                EmInCo.UserSelection = tk.Label(EmInCo.frame, text="Employee ID", font=("Georgia", 20), fg='black')
                EmInCo.UserSelection.grid(row=0,column=0)
                EmInCo.SearchButton = tk.Button(EmInCo.frame, text="Search", command=SearchDB)
                EmInCo.SearchButton.grid(row=1, column=0)
                EmInCo.ReturnToMenu = tk.Button(EmInCo.frame, text="Return to selection",command=ReturnToSelection).grid(row=1, column=1)
               
                EmInCo.EIDEntry = tk.Entry(EmInCo.frame) #ID entry by user
                EmInCo.EIDEntry.grid(row=0, column=1)


       
            EmInCo.TitleDisplay_label = tk.Label(EmInCo.frame, text="Employee Information Collection",font=("Arial", 30)) #Title for mainscreen
            EmInCo.TitleDisplay_label.place(x=175, y=50)
           
           
            EmInCo.btn = tk.Button(EmInCo.frame, text='Add New Employee', command=AddNewEmployee, font=("Georgia", 20), bg ='#999999', fg = 'black', height=2, width=20) #Button for mainscreen
            EmInCo.btn.place(x=300, y=300)

            EmInCo.btn2 = tk.Button(EmInCo.frame, text='Search/Change ', command=SearchAndEdit, font=("Georgia", 20), bg='#999999', fg = 'black', height = 2, width=20) #Button for mainscreen
            EmInCo.btn2.place(x=300, y=175)
       
        Outer()
    def run(EmInCo): #Runs the loop
        EmInCo.window.mainloop()

EmInCoRun = EICOuter()
EmInCoRun.run()
