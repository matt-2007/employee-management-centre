"""Creates EmployeeManagementCenter.db with the tables the program expects.

Run this once before starting the program:
    python setup_database.py
"""
import sqlite3
from pathlib import Path

DB_NAME = "EmployeeManagementCenter.db"
SCHEMA = Path(__file__).with_name("schema.sql").read_text()

with sqlite3.connect(DB_NAME) as conn:
    conn.executescript(SCHEMA)

print(f"Created {DB_NAME} with tables: Logins, EmployeeInformation, EmployeeLeave")
