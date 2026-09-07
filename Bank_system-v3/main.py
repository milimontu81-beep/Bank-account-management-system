# Bank account management system 
import sqlite3
connection=sqlite3.connect("bank.db")
cursor=connection.cursor()
#create a table with column accountnumber, username, phonenumber, password ,balance
cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(accountnumber INTEGER PRIMARY KEY,username TEXT,phonenumber INTEGER,password TEXT,balance INTEGER)""")
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
        if Bal_ance[0] is None or Bal_ance is None:
          Balance=0
        else:
          Balance=Bal_ance[0]
        print("==BALANCE==")
        print("-BALANCE RS.",Balance)
        print("------------------------------------")   
#save the transaction history of the account 
      def see_history(self,history,accountnumber,balanceafter):
        Bal_ance=cursor.execute("""SELECT balance FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
        Ba_lance=Bal_ance[0]
        if Ba_lance is None or Ba_lance is None:
          Balance=0
        else:
          Balance=Ba_lance
#save the transaction history into sql database        
          cursor.execute(f"""INSERT INTO "{accountnumber}"(history,balancebefore,balanceafter) 
        VALUES(?,?,?)""",(history,Balance,balanceafter))
        connection.commit()

#take user input for login or create account 
#manage the bank account operations
def ACCOUNT(accountnumber):
  Bal_ance=cursor.execute("""SELECT balance FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
  if Bal_ance[0] is None:
    Balance=0
  else:
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
   try:
#take the menu user choice
    choice = int(input("-Enter your choice :"))
    print("------------------------------------")
#using conditional statements to perform the operation according to the user choice 
#credit money to the account
    if choice==1:
      print("==CREDIT==")
      process="credited"
      amount=int(input(f"-Enter the amount to be {process} Rs."))
      balance=cursor.execute("""SELECT balance FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
      ba_lance=balance[0]
      if ba_lance is None or ba_lance is None:
        bala_nce=0
      else:
        bala_nce=ba_lance
      balanceafter=bala_nce+amount
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
      bala_nce=balance[0]
      if bala_nce is None or bala_nce is None:
        ba_lance=0
      else:
        ba_lance=bala_nce
      if ba_lance<amount:
        print("-Insufficient balance!")
        print("------------------------------------")
      
      balanceafter=bala_nce-amount
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
      history=cursor.execute(f"""SELECT history FROM "{accountnumber}" """).fetchone()
      History=cursor.execute(f"""SELECT * FROM "{accountnumber}" """).fetchall()
      if history[0] is None:
         print(" No transaction history found!")
      else: 
         print("-Transaction history:")