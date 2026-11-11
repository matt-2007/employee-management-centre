import random
from tkinter import *
import tkinter as tk
import time
from tkinter.ttk import *
import tkinter.filedialog
import os
import sys
import sqlite3
import bcrypt

class LoginOuter:
    def __init__(login):
        login.window = tk.Tk() #Sets window attributes
        login.window.title("Login Page")
        login.window.geometry("500x500")    #sets window size
        login.window.attributes('-fullscreen', False)
        login.window.configure(bg = "#efefef") #sets window background colour
        login.frame = Frame(login.window)
        login.frame.pack(side="top", expand=True, fill="both")

       

        def createlogin():
            for login.widgets in login.frame.winfo_children(): #Clears the frame
                login.widgets.destroy()

            def loginentry():
                login.passget = login.password.get() #Takes user entry and .gets's
                login.test = bytes(login.passget, encoding='utf-8')
                login.salt = b'$2b$12$RNEhJURFjbN42veQmKeRh.' #Combines with byte value of salt
                login.hashedP = bcrypt.hashpw(login.test, login.salt) #Encrypts using bcrypt

                login.manpassget = login.managementpass.get() #Gets user entered management password
                login.temphold = bytes(login.manpassget, encoding="utf-8")
                login.hashedMP = bcrypt.hashpw(login.temphold, login.salt) #Hashes user entered management password

                def retry():
                    for Login.widgets in Login.frame.winfo_children(): #Clears frame
                        Login.widgets.destroy()
                    createlogin()

                def retrybutton():
                    Login.Retry_button = tk.Button(Login.frame, text="Retry", command=retry).grid(row=4,column=1, sticky=tk.W, pady=4)

                login.usernameget = login.username.get()

                login.PresenceCheck = True
                login.DataEntryAccept = True
                while login.PresenceCheck == True: #Checks for empty inputs
                    if login.username.get() == "":
                        login.Errorbox1 = tk.Label(login.frame, text="Username cannot be blank", font=("Georgia", 10), fg="black").grid(row=3, column=0)
                        login.PresenceCheck = False
                        login.DataEntryAccept = False
                    if login.password.get() == "":
                        login.Errorbox2 = tk.Label(login.frame, text="Password cannot be blank", font=("Georgia", 10), fg="black").grid(row=4, column=0)
                        login.PresenceCheck = False
                        login.DataEntryAccept = False
                    break
                if Login.PresenceCheck == False: #If found then force retry + halt data entry
                    retrybutton()

                login.isManagement = False
                def isManagementCheck(): #Check if management password present
                    if login.hashedMP == b'$2b$12$RNEhJURFjbN42veQmKeRh.oFcTY3yQ.SrljYU7NmeLCPKW1GDkd1C': #Checks if management hash is same as predefined
                        login.isManagement = True #If true then set to true
                    else:
                        login.DataEntryAccept = False
                        login.Errorbox4 = tk.Label(login.frame, text="Management password is wrong", font=("Georgia", 10), fg="black").grid(row=2, column=2)
                        retrybutton()

                if len(login.managementpass.get()) != 0: #Only runs check if user put something in managementpassword entry box
                        isManagementCheck()
                 


                if login.DataEntryAccept == True:
                    try: #Inserting the new values into database
                        sqliteConnection = sqlite3.connect("EmployeeManagementCenter.db")
                        cursor = sqliteConnection.cursor()

                        cursor.execute("INSERT INTO Logins (username, password, management) VALUES(?,?,?)", (login.usernameget, login.hashedP, login.isManagement));
                        sqliteConnection.commit()
                        cursor.close()
                    except sqlite3.Error as error:
                        print("Error occured - ", error)
                    finally:
                        if sqliteConnection:
                            sqliteConnection.close()
                else:
                    Login.Errorbox3 = tk.Label(login.frame, text="Data has not been stored", font=("Georgia", 10), fg="black").grid(row=5, column=0) #Incase of error shows that it isnt stored
           
            def tologinbutton():
                loginpre()

            login.createuser_entry = tk.Label(login.frame, text="Username", font=("Georgia", 20), fg = 'black').grid(row=0) #Creates labels
            login.createpassword_entry = tk.Label(login.frame, text="Password", font=("Georgia", 20), fg = 'black').grid(row=1)
            login.createmanagement_entry = tk.Label(login.frame, text="Management",font=("Georgia", 20),fg="black").grid(row=2)
            login.Ok_button = tk.Button(login.frame, text='Ok', command=loginentry).grid(row=3, column=1, sticky=tk.W, pady=4)
            login.Back_buttonCreate = tk.Button(login.frame, text="Login", command=tologinbutton).grid(row=3, column=2,sticky=tk.W, pady=4)

            login.username = tk.Entry(login.frame) #Creates entry boxes
            login.password = tk.Entry(login.frame)
            login.managementpass = tk.Entry(login.frame)

            login.username.grid(row=0, column=1) #Places entry boxes
            login.password.grid(row=1, column=1)
            login.managementpass.grid(row=2, column=1)

           
        def loginpre(): #Used for login
            for login.widgets in login.frame.winfo_children(): #Clears the frame
                login.widgets.destroy()

            def PreOkButton():
                def RetryButton():
                    login.RetryButton = tk.Button(login.frame, text="Retry", command=loginpre).grid(column=1, row=3)

                login.dblogincheck = True

                login.userentryget = login.userentry.get() #.get of user entered data
                login.loginpassget = login.passentry.get()
                if login.userentryget == "":
                    login.errorbox = tk.Label(login.frame, text="Username cannot be blank", font=("Georgia", 20), fg="black").grid(column=0, row=4) #Error check for presence
                    login.dblogincheck = False
                    RetryButton()
                   
                if login.loginpassget == "":
                    login.errorbox2 = tk.Label(login.frame, text="Password cannot be blank", font=("Georgia", 20), fg="black").grid(column=0, row=5) #Error check for presence
                    RetryButton()

                login.PasswordBytes = bytes(login.loginpassget, encoding='utf-8') #Hashes the users entry to check against hashed value held on database
                login.CheckSalt = b'$2b$12$RNEhJURFjbN42veQmKeRh.'
                login.HashPassCheck = bcrypt.hashpw(login.PasswordBytes, login.CheckSalt)


                if login.dblogincheck == True:
                    try: #Selects row where username is same as userentryget
                        sqliteConnection = sqlite3.connect("EmployeeManagementCenter.db")
                        cursor = sqliteConnection.cursor()
                        cursor.execute("SELECT * FROM Logins WHERE username = ?", (login.userentryget,));
                        row = cursor.fetchone()
                       
                        try:
                            if login.HashPassCheck ==  row[1]: #if hashes are same then correct login
                                print("Correct login")
                            elif login.HashPassCheck != row[1]:
                                login.loginstatus = tk.Label(login.frame, text="Incorrect username or password", font=("Georgia", 20), fg='black').grid(column=0, row=10) #else one is incorrect
                        except:
                            login.loginstatus2 = tk.Label(login.frame, text="Username not found", font=("Georgia", 20), fg='black').grid(column=0, row=12) #identify if username not found

                        sqliteConnection.commit()
                        cursor.close()
                    except sqlite3.Error as error:
                        print("Error occured - ", error) #display any sql errors
                    finally:
                        if sqliteConnection:
                            sqliteConnection.close()

            login.loginuser_entry = tk.Label(login.frame, text="Username", font=("Georgia", 20), fg = 'black').grid(row=0) #creates labels
            login.loginpass_entry = tk.Label(login.frame, text="Password", font=("Georgia", 20), fg = 'black').grid(row=1)
            login.PreOk_button = tk.Button(login.frame, text='Ok', command=PreOkButton).grid(row=3, column=0, sticky=tk.W, pady=4)
           

            login.userentry = tk.Entry(login.frame) #entry boxes for username and password
            login.passentry = tk.Entry(login.frame)

            login.userentry.grid(row=0, column=1) #places entry boxes
            login.passentry.grid(row=1, column=1)

        login.choice_button1 = tk.Button(login.frame, text="Create Login", command=createlogin).grid(row=0, column=0, sticky=tk.W, pady=4) #buttons to choose between createlogin or just login
        login.choice_button2 = tk.Button(login.frame, text="Login", command=loginpre).grid(row=0,column=1,stick=tk.W,pady=4)


    def run(login):#runs loop
        login.window.mainloop()

Login = LoginOuter()
Login.run()
