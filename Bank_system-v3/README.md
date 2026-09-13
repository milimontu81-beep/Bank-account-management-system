# Bank Account Management System

A Python-based Bank Account Management System using SQLite database.

## Features

- Create multiple bank accounts
- Login using account number, username and password
- Credit money
- Debit money
- Check account balance
- View transaction history
- Store transaction amount
- Store balance before and after transactions
- Automatic transaction date and Indian time
- SQLite database integration
- Primary Key and Foreign Key
- Default account balance
- Input validation
- Exception handling
- Database transaction rollback
- Object-Oriented Programming

## Technologies Used

- Python
- SQLite3(python builtin module)

## Database Structure

### Accounts Table

Stores account information:

- Account Number
- Username
- Phone Number
- Password
- Balance

### History Table

Stores transaction information:

- Transaction ID
- Account Number
- Transaction Type
- Amount
- Balance Before
- Balance After
- Time
- Date

The History table is connected to the Accounts table using a Foreign Key.

## Concepts Used

- Python Classes and Objects
- Functions
- Loops
- Conditional Statements
- Exception Handling
- SQLite3
- SQL CREATE
- SQL INSERT
- SQL SELECT
- SQL UPDATE
- Primary Keys
- Foreign Keys
- DEFAULT Values
- fetchone()
- fetchall()
- commit()
- rollback()

## Future Improvements

- Password hashing
- Delete account
- Update account details
- Transaction search by date
- ORDER BY transaction history
- Improved login system
- GUI or web interface