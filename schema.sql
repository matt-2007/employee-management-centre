-- Database schema for the Employee Management Centre.
-- The original tables were created by hand in DB Browser for SQLite;
-- this file recreates them from the columns the code reads and writes.

CREATE TABLE IF NOT EXISTS Logins (
    username   TEXT PRIMARY KEY,
    password   BLOB NOT NULL,          -- bcrypt hash
    management BOOLEAN NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS EmployeeInformation (
    employeeid  INTEGER PRIMARY KEY,
    firstname   TEXT,
    surname     TEXT,
    age         INTEGER,
    gender      TEXT,
    status      TEXT,
    jobtitle    TEXT,
    phonenumber TEXT,
    email       TEXT,
    salary      REAL
);

CREATE TABLE IF NOT EXISTS EmployeeLeave (
    leaveid    INTEGER PRIMARY KEY,
    employeeid INTEGER,
    firstname  TEXT,
    surname    TEXT,
    leavetype  TEXT,
    reason     TEXT,
    leavestart TEXT,
    leaveend   TEXT,
    status     TEXT
);
