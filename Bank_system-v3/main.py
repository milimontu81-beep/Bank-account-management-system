 # Bank account management system 
import sqlite3
connection=sqlite3.connect("bank.db")
cursor=connection.cursor()
#create a table with column accountnumber, username, phonenumber, password ,balance
cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(accountnumber INTEGER PRIMARY KEY,username TEXT NOT NULL,phonenumber INTEGER NOT NULL,password TEXT NOT NULL,balance INTEGER NOT NULL DEFAULT 0)""")
#create a table with column id ,acountnumber,history,balancebefore,balanceafter,time,date
cursor.execute("""CREATE TABLE IF NOT EXISTS history(id INTEGER PRIMARY KEY AUTOINCREMENT,accountnumber INTEGER NOT NULL,history TEXT NOT NULL,balancebefore INTEGER NOT NULL,balanceafter INTEGER NOT NULL,time INTEGER NOT NULL DEFAULT (TIME('now','+5 hours','+30 minutes')),date INTEGER NOT NULL DEFAULT (DATE('now','+5 hours','+30 minutes')))""")
connection.commit()
tables=cursor.execute("""SELECT name FROM sqlite_master WHERE type='table'""").fetchall() 
# create a account class with attributes account number and balance    
class Account:
      def __init__(self, act_no, balance):
       self.act_no = act_no
       self.balance = balance      
#withdraw money from the account 
      def credit(self, amount):
       if amount<0:
        print("-Invalid amount!")
        print("------------------------------------")
       else:
        print("-Your account has been debited with Rs.",amount)
        print("------------------------------------")       
#show the balance of the account 
      def see_balance(self):
        Bal_ance=cursor.execute("""SELECT balance FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
        Balance=Bal_ance[0]
        print("==BALANCE==")
        print("-BALANCE RS.",Balance)
        print("------------------------------------")   
#save the transaction history of the account 
      def see_history(self,history,accountnumber,balanceafter):
        Bal_ance=cursor.execute("""SELECT balance FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
        Balance=Bal_ance[0]
#save the transaction history into sql database        
        cursor.execute("""INSERT INTO history(accountnumber,history,balancebefore,balanceafter) 
        VALUES(?,?,?,?)""",(accountnumber,history,Balance,balanceafter))
        connection.commit()

#take user input for login or create account 
#manage the bank account operations
def ACCOUNT(accountnumber):
  Bal_ance=cursor.execute("""SELECT balance FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
  Balance=Bal_ance[0]
#create an object of the account class
  account=Account(accountnumber,Balance)
  print("===WELCOME TO THE BANK===")
  us_ername=cursor.execute("""SELECT username FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
  pho_nenumber=cursor.execute("""SELECT phonenumber FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
  print("-USERNAME:",us_ername[0])
  print("-ACCOUNT NUMBER:",accountnumber)
  print("-PHONE NUMBER:",pho_nenumber[0])
  print("-BALANCE RS.",Balance)
#A menu driven program that allows the user to credit or debit the account
  print("ENTER-1-CREDIT")
  print("ENTER-2-DEBIT") 
  print("ENTER-3-SEE BALANCE")
  print("ENTER-4-SEE TRANSACTION HISTORY")
  print("ENTER-5-LOGOUT") 
#create a loop to run the program until the user exits
  while True:
#to handle invalid input
   #try:
#take the menu user choice
    choice = int(input("-Enter your choice :"))
    print("------------------------------------")
#using conditional statements to perform the operation according to the user choice 
#credit money to the account
    if choice==1:
      print("==CREDIT==")
      process="credited"
      amount=int(input(f"-Enter the amount to be {process} Rs."))
      if amount<=0:
        print("Invalid amount!")
        print("------------------------------------")
      else:
        ba_lance=cursor.execute("""SELECT balance FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
        Balance=ba_lance[0]
        balanceafter=Balance+amount
        history=f"{process} with Rs.{amount}"
        account.see_history(history,accountnumber,balanceafter)
        cursor.execute("""UPDATE accounts SET balance=? WHERE accountnumber=?""",(balanceafter,accountnumber))
        connection.commit()
        print("-Your account has been credited with rs.",amount)
        print("------------------------------------")
#debit money from the account
    elif choice==2:
      print("==DEBIT==")
      process="debited"
      amount=int(input(f"-Enter the amount to be {process} Rs."))
      balance=cursor.execute("""SELECT balance FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
      Balance=balance[0]
      if Balance<amount:
        print("-Insufficient balance!")
        print("------------------------------------")
      elif amount<=0:
        print("Invalid amount!")
        print("------------------------------------")
      else:
        balanceafter=Balance-amount
        history=f"{process} with Rs.{amount}"
        account.see_history(history,accountnumber,balanceafter)
        cursor.execute("""UPDATE accounts SET balance=? WHERE accountnumber=?""",(balanceafter,accountnumber))
        connection.commit()
        print("-Your account has been debited with rs.",amount)
        print("------------------------------------")
#logout the account
    elif choice==5:
      print("==THANKS FOR USING OUR BANK==")
      print("------------------------------------")
      break 
#show balance after each transaction
    elif choice==3:
      account.see_balance()
#show transaction history 
    elif choice==4:
      print("==TRANSACTION HISTORY==")
      History=cursor.execute(f"""SELECT 1 FROM history WHERE accountnumber=?""",(accountnumber,)).fetchone()
      history=cursor.execute(f"""SELECT * FROM history WHERE accountnumber=?""",(accountnumber,)).fetchall()
      if History:
        print("-Transaction history:")
        count=1
        for i in history:
           print(f"{count}.{i[2]},balancebefore Rs.{i[3]},balanceafter Rs.{i[4]},time:{i[5]},date:{i[6]}")
           count+=1
        print("------------------------------------")
      else: 
        print(" No transaction history found!")      
#handle invalid input
    else:  
      print("-Invalid choice: please enter a no. between 1 to 5!")
      print("------------------------------------")
   except:
     print("-Invalid input:please enter an integer!")
     print("------------------------------------")
#save the account information after account has been created
def createaccount():
     cursor.execute("""INSERT INTO accounts(accountnumber,username,password,phonenumber)
     VALUES(?,?,?,?)""",(accountnumber,username, password,phonenumber))
     connection.commit()
     user_name=username.upper()
     print(f"-''{user_name}', your  account has been created successfully!")
     print("-Your account number is:",accountnumber)
     print("-Your password is:",password)
     print("-Your phone number is:",phonenumber)
     print("------------------------------------") 
#menu of the bank account management system 
print("===WELCOME TO THE BANK OF INDIA===")
print("ENTER-1-LOGIN")
print("ENTER-2-CREATE ACCOUNT ")
print("ENTER-3-EXIT")
#create a loop to run the program until the user exits
while True:
#to handle invalid input
 try:
#take the menu user choice
  choice=int(input("-ENTER YOUR CHOICE:"))
  print("------------------------------------")
  if choice==1:
    print("===LOGIN===")
#take the user input for login
    try:
      username=input("-ENTER YOUR USERNAME:")
      accountnumber=input("-ENTER YOUR ACCOUNT NUMBER:")
      password=input("-ENTER YOUR PASSWORD:")    
      na_me=cursor.execute("""SELECT username FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
      name=na_me[0]
      pass_word=cursor.execute("""SELECT password FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
      accountnumberlist=cursor.execute("""SELECT 1 FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchall()
      userpassword=pass_word[0]
#check if the account match or exist for login
      if accountnumberlist and username == name and password == userpassword:
#call the account function to perform the operations
       ACCOUNT(accountnumber)
      else:
        print("-ACCOUNT NOT FOUND!")
        print("------------------------------------")
    except:
        print("-ACCOUNT NOT FOUND!")
        print("------------------------------------")
#create account
  elif choice==2:
   
    print("===CREATE ACCOUNT===")
#take the user input for creating account
 