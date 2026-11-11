# Employee Management Centre

A desktop app for managing employee records and leave requests, built in Python with a Tkinter interface and an SQLite database.

I built it during sixth form as my A-level Computer Science project (2024–25). It was developed for a client who needed one place to store staff details, handle leave requests, and keep logins secure. The project went through the full process: research into existing products, requirements, design, development, testing and client reviews.

## Features

**Login**
- Create an account and log in with a username and password
- Passwords are hashed with **bcrypt** before they are stored, never saved as plain text
- Separate management accounts, created with a management password
- Validation for empty fields, wrong passwords and unknown usernames

**Employee information**
- Add new employees: ID, name, age, gender, status, job title, phone number, email and salary
- Search for an employee by ID and edit any single field
- Input validation (for example, numeric checks on IDs, age and salary) with clear error messages

**Leave management**
- Employees can submit leave requests (annual, sick, maternity or paternity leave) with start and end dates picked from a calendar
- Managers can view pending requests one at a time and approve or deny them

All database queries use **parameterised SQL** (`?` placeholders) to protect against SQL injection.

## Tech

- Python 3
- Tkinter / ttk for the interface, with [tkcalendar](https://pypi.org/project/tkcalendar/) for date pickers
- SQLite (`sqlite3`)
- bcrypt for password hashing

## Project structure

| File | What it does |
|---|---|
| `MainMenu.py` | Start screen with Login and Instructions buttons |
| `Login.py` | Account creation and login, with bcrypt hashing |
| `EmployeeInformation.py` | Add, search and edit employee records |
| `LeaveManagement.py` | Create leave requests and approve or deny pending ones |
| `schema.sql` | Table definitions for the database |
| `setup_database.py` | Creates `EmployeeManagementCenter.db` from `schema.sql` |

## Running it

```bash
pip install -r requirements.txt
python setup_database.py       # creates the database (run once)
python MainMenu.py             # or run any module directly, e.g. python Login.py
```

Each module is its own window and can be run directly. The main menu opens `Login.py` using `os.system`, which works on Windows when `.py` files are set to open with Python. On macOS or Linux, run the modules directly instead.

Note: in the original project the database tables were created by hand in DB Browser for SQLite. `schema.sql` recreates them from the columns the code uses, so the app can be set up from a fresh clone.

## Status and known limitations

This is the project as I submitted it. I've left the code unchanged so it shows where I was at the time. Things I know are missing or could be better:

- **The modules aren't fully linked together.** The main menu closes and opens the login window, and inside each module the buttons switch between screens. But a successful login only confirms the details. It doesn't open the employee or leave modules, and access levels aren't enforced in them. `Instructions.py` was planned but never written.
- **A fixed bcrypt salt.** Every password is hashed with the same salt. The right approach is `bcrypt.gensalt()` when creating an account and `bcrypt.checkpw()` when logging in, so each password gets its own salt.
- **The management password check compares against a hard-coded hash** in the source code. This would be better kept in configuration or the database.
- **Password fields show the text as you type.** They should use `show="*"`.
- **There is a lot of repeated code.** For example, there is a near-identical function for editing each employee field. A single function driven by a list of fields would cut the code down a lot.
- **Structure.** Most logic is nested inside each window's `__init__`, and a new database connection is opened for each action. Separating the database code from the UI (and using classes properly) would make it easier to test and extend.
- Two planned features, employee reputation (commendations and reports) and performance management, were dropped because of time.

## What I'd do in a rewrite

1. Put the modules into one app with a single window and proper navigation after login
2. Add a separate data-access layer for all SQL, with unit tests
3. Per-user salts, `checkpw`, and hidden password input
4. Replace the repeated field functions with one generic edit function
5. Role-based access so only managers can approve leave and edit records
