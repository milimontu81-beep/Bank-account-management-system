# Bank Account Management System

## Version 1

A simple Python-based Bank Account Management System.

### Features

- Credit money
- Debit money
- View balance
- View transaction history

### How It Works

- Enter `1` → Credit money
- Enter `2` → Debit money
- Enter `3` → View balance
- Enter `4` → View transaction history
- Enter `5` → Exit

### Technology Used

- Python 3

## How to Run

### Requirements
- Python 3.x
- No external libraries required

### Steps

1. Open the `Bank_system-v1` folder.
2. Download `main.py`.
3. Run `bank_system.py` using Python 3. 
4. Follow the instructions shown in the terminal.

---

## Version 2

An upgraded version of the Python Bank Account Management System with JSON file handling and support for multiple users.

### Features

- User-friendly menu
- Create an account
- User login
- Support for multiple users
- Credit money
- Debit money
- Persistent balance
- Transaction history
- JSON-based data storage
- Account and user information validation

### How It Works

#### First Menu

- Enter `1` → Login
- Enter `2` → Create Account
- Enter `3` → Exit

#### Account Menu

After successfully logging in:

- Enter `1` → Credit money
- Enter `2` → Debit money
- Enter `3` → View balance
- Enter `4` → View transaction history
- Enter `5` → Logout

### Technology Used

- Python 3
- JSON (built-in Python module)

## How to Run

### Requirements
- Python 3.x
- No external libraries required

### Steps

1. Open the `Bank_system-v2` folder.
2. Download `main.py`and `bank_data.json`.
3. Keep both files in the same folder.
4. Run `main.py` using Python 3.
5. Follow the instructions shown in the terminal.

---

## Version 3

An upgraded version of the Bank Account Management System using Python and SQLite database.

Version 3 replaces JSON file storage with an SQLite database and introduces relational database concepts.

### Features

- Create multiple accounts
- User login
- Account logout
- Credit money
- Debit money
- View account balance
- View transaction history
- Support for multiple users
- Persistent data storage using SQLite
- Automatic Indian time and date for transactions
- Store balance before and after each transaction
- Account number validation
- Password validation
- Phone number validation
- Exception handling
- SQLite database error handling
- Database transaction rollback
- Primary Key and Foreign Key
- Object-Oriented Programming

### Database Structure

#### Accounts Table

Stores account information:

- Account Number
- Username
- Phone Number
- Password
- Balance

The account number is used as the Primary Key.

#### History Table

Stores transaction information:

- Transaction ID
- Account Number
- Transaction Type
- Amount
- Balance Before Transaction
- Balance After Transaction
- Time
- Date

The account number in the History table is connected to the Accounts table using a Foreign Key.

### How It Works

#### First Menu

- Enter `1` → Login
- Enter `2` → Create Account
- Enter `3` → Exit

#### Account Menu

After successfully logging in:

- Enter `1` → Credit money
- Enter `2` → Debit money
- Enter `3` → View balance
- Enter `4` → View transaction history
- Enter `5` → Logout

### Technology Used

- Python 3
- SQLite3

### SQL Concepts Used

- CREATE TABLE
- INSERT
- SELECT
- UPDATE
- PRIMARY KEY
- FOREIGN KEY
- DEFAULT values
- fetchone()
- fetchall()
- commit()
- rollback()

### Exception Handling Used

- ValueError
- sqlite3.IntegrityError
- sqlite3.Error

## How to Run

### Requirements

- Python 3.x
- SQLite3 (included with Python)

### Steps

1. Open the `Bank_system-v3` folder.
2. Download `main.py`.
3. Run `main.py` using Python 3.
4. The `bank.db` database file will be created automatically.
5. Follow the instructions shown in the terminal.
---

## Version 4

An improved version of the Bank Account Management System with enhanced security, account management, and transaction search features.

Version 4 builds on Version 3 by adding password hashing, hidden password input, account settings, transaction filtering, and account deletion.

### Improvements

- Password hashing using Argon2
- Password verification using Argon2
- Hidden password input using `getpass`
- View account profile
- Change password
- Change phone number
- Search transaction history by date
- Filter transaction history by credit or debit
- Delete account
- Automatic deletion of related transaction history using `ON DELETE CASCADE`
- Improved password validation
- Improved account management
- Improved input validation
- Improved error handling

### Account Settings

After logging in, users can manage their account through the settings menu.

Available options include:

- View profile
- Change password
- Change phone number
- Search transaction history by date
- Filter transactions by credit or debit
- Delete account
- Return to account menu

### Password Security

Version 4 improves password security by using **Argon2** for password hashing and verification.

Passwords are not stored as plain text in the database.

The `getpass` module is also used to hide password input during login and sensitive account operations.

### Transaction Search

Users can search their transaction history using:

- Specific date
- Credit transactions
- Debit transactions

This makes it easier to find specific transactions without displaying the entire transaction history.

### Account Deletion

Users can permanently delete their account after password verification.

When an account is deleted, its related transaction history is automatically deleted from the database using:

`ON DELETE CASCADE`

### Technology Used

- Python 3
- SQLite3
- SQL
- Argon2
- `getpass`
- Object-Oriented Programming (OOP)

## How to Run

### Requirements

- Python 3.x
- SQLite3 (included with Python)

### Steps

1. Open the `Bank_system-v3` folder.
2. Download `main.py`.
3. Run `main.py` using Python 3.
4. The `bank.db` database file will be created automatically.
5. Follow the instructions shown in the terminal.

### Project Progression

Version 3 is an upgrade of Version 2. It replaces JSON file storage with an SQLite database and adds relational database concepts such as Primary Keys and Foreign Keys.

The project has progressed from:

**Version 1 → Basic Python Bank System**

**Version 2 → JSON File Handling and Multiple Users**

**Version 3 → SQLite Database and Relational Database Management**

**Version 4 → Password Security, Account Management, and Transaction Search**

Version 4 improves the Version 3 SQLite-based system by adding better password security and more account-management features.





