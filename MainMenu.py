import random
from tkinter import * #imports all tkinter libraries
import tkinter as tk
import time
from tkinter.ttk import *
import tkinter.filedialog
import os #import to use file handling
import sys  #imports for all required python libraries

class mainMenuOuter: #outer class
    def __init__(mainmenu): #procedure to create the window
        mainmenu.window = tk.Tk()
        mainmenu.window.title("Main Menu") #sets window name
        mainmenu.window.geometry("1920x1080")    #sets window size
        mainmenu.window.attributes('-fullscreen', True)
        mainmenu.window.configure(bg = "#efefef") #sets window background colour


        mainmenu.test_label = tk.Label(mainmenu.window, text="Employee Management Centre", font=("Georgia", 40))  
        mainmenu.test_label.pack(pady=200) #sets label padding from edge of window
        mainmenu.test_label.configure(bg = "#efefef", fg = "black") #sets label background and foreground

       
        mainmenu.pyexec = sys.executable          

        def run_program(): #handles what happens when login button is pressed
            mainmenu.window.destroy() #closes current window
            os.system("Login.py") #opens login window
       
        mainmenu.btn = tk.Button(mainmenu.window, text='Login', command=run_program, font=("Georgia", 30), bg ='#999999', fg = 'black', height=2, width=10) #defines button along with its parameters

        def run_program2():
            pass
            mainmenu.window.destroy() #closes current window
            os.system("Instructions.py") #opens instructions window
       
        mainmenu.btn2 = tk.Button(mainmenu.window, text='Instructions',  command=run_program2, font=("Georgia", 30), bg ='#999999', fg = 'black', height=2, width=10)

        mainmenu.btn.place(x=500, y=300) #location on window of button
        mainmenu.btn2.place(x=500, y=500)


    def run(mainmenu): #loops until the user closed the window
        mainmenu.window.mainloop()

       

MainMenu = mainMenuOuter() #defines mainMenuOuter as MainMenu
MainMenu.run() #runs MainMenu
