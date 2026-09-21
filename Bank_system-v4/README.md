# Bank Account Management System

A Python-based bank account management system built using SQLite. This project allows multiple users to create accounts, securely log in, manage their balance, and view their transaction history.

## Features

- Create a new bank account
- Multiple user accounts
- Login and logout
- Credit money
- Debit money
- Check account balance
- View transaction history
- Search transaction history by date
- Filter transactions by credit or debit
- View account profile
- Change password
- Change phone number
- Delete account
- Persistent data using SQLite
- Password hashing using Argon2
- Hidden password input using `getpass`
- Input validation
- Exception handling
- Automatic deletion of transaction history when an account is deleted

## Technologies Used

- Python
- SQLite
- SQL
- Argon2
- `getpass`
- Object-Oriented Programming (OOP)

## Database

The project uses SQLite to store account and transaction data.

The database contains information such as:

- Account number
- Username
- Phone number
- Hashed password
- Account balance
- Transaction type
- Transaction amount
- Balance before and after transactions
- Transaction date and time

## Security

Passwords are not stored as plain text.

The project uses **Argon2** for password hashing and verification.

`getpass` is used to hide password input in the terminal during login and other sensitive account operations.

The stored password is a secure Argon2 hash, while the original password is never stored directly in the database.

## How It Works

1. Create a new account.
2. Enter the required account information and password.
3. The password is hashed using Argon2 before being stored.
4. Login using the account number and password.
5. Perform banking operations such as crediting and debiting money.
6. View the current account balance.
7. View or search transaction history.
8. Manage account information through the settings menu.
9. Delete the account when required.

## SQL Features Used

This project helped me practice SQL and database concepts such as:

- `CREATE TABLE`
- `INSERT`
- `SELECT`
- `UPDATE`
- `DELETE`
- `WHERE`
- Primary keys
- Foreign keys
- `ON DELETE CASCADE`

## What I Learned

Through this project, I practiced:

- Python Object-Oriented Programming
- SQLite database management
- SQL queries
- Database relationships
- Persistent data storage
- Password hashing and verification
- Secure password input using `getpass`
- Input validation
- Exception handling
- Working with multiple users
- Managing transaction records
- Designing a complete console-based application

## Future Improvements

Possible future improvements include:

- Web-based interface
- REST API integration
- Email or SMS notifications
- More advanced transaction searching and filtering
- Improved authentication and authorization

## Note

This project was created as a learning and portfolio project to practice Python, SQL, SQLite, authentication, and database management.

It is not intended to be used as a real banking system.

## Author

**Montu Mili**