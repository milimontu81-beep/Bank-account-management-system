# Bank account management system 
from getpass import getpass
from argon2 import PasswordHasher
ph=PasswordHasher()
import sqlite3
connection=sqlite3.connect("bank.db")
connection.execute("PRAGMA foreign_keys=ON")
cursor=connection.cursor()
#create a table with column accountnumber, username, phonenumber, password ,balance
cursor.execute("""CREATE TABLE IF NOT EXISTS accounts(accountnumber INTEGER PRIMARY KEY,username TEXT NOT NULL,phonenumber TEXT NOT NULL,password TEXT NOT NULL,balance INTEGER NOT NULL DEFAULT 0)""")
#create a table with column id ,acountnumber,history,balancebefore,balanceafter,time,date
cursor.execute("""CREATE TABLE IF NOT EXISTS history(id INTEGER PRIMARY KEY AUTOINCREMENT,accountnumber INTEGER NOT NULL,history TEXT NOT NULL,amount INTEGER NOT NULL,balancebefore INTEGER NOT NULL,balanceafter INTEGER NOT NULL,time TEXT NOT NULL DEFAULT (TIME('now','+5 hours','+30 minutes')),date TEXT NOT NULL DEFAULT (DATE('now','+5 hours','+30 minutes')) ,FOREIGN KEY (accountnumber)
REFERENCES accounts(accountnumber)
ON DELETE CASCADE)""")
connection.commit()
# create a account class with attributes account number and balance    
class Account:
      def __init__(self, act_no, balance):
       self.act_no = act_no
       self.balance = balance            
#show the balance of the account 
      def see_balance(self):
        Bal_ance=cursor.execute("""SELECT balance FROM accounts WHERE accountnumber=?""",(self.act_no,)).fetchone()
        Balance=Bal_ance[0]
        print("==BALANCE==")
        print("-BALANCE RS.",Balance)
        print("------------------------------------")   
#save the transaction history of the account 
      def see_history(self,history,accountnumber,amount,balanceafter):
        Bal_ance=cursor.execute("""SELECT balance FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
        Balance=Bal_ance[0]
#save the transaction history into sql database        
        cursor.execute("""INSERT INTO history(accountnumber,history,amount,balancebefore,balanceafter) 
        VALUES(?,?,?,?,?)""",(accountnumber,history,amount,Balance,balanceafter))
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
  print("ENTER-5-SETTINGS")
  print("ENTER-6-LOGOUT") 
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
     try:
      amount=int(input(f"-Enter the amount to be {process} Rs."))
      if amount<=0:
        print("Invalid amount!")
        print("------------------------------------")
      else:
        ba_lance=cursor.execute("""SELECT balance FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
        Balance=ba_lance[0]
        balanceafter=Balance+amount
        history=f"{process}"
     
        account.see_history(history,accountnumber,amount,balanceafter)
        cursor.execute("""UPDATE accounts SET balance=? WHERE accountnumber=?""",(balanceafter,accountnumber))
        connection.commit()
        print("-Your account has been credited with rs.",amount)
        print("------------------------------------")
     except ValueError:
        print("Please,enter an valid amont! ")
        print("------------------------------------")
     except sqlite3.Error as e:
       connection.rollback()
       print("Transaction failed:",e)
#debit money from the account
    elif choice==2:
     print("==DEBIT==")
     process="debited"
     try:
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
        history=f"{process}"
        account.see_history(history,accountnumber,amount,balanceafter)
        cursor.execute("""UPDATE accounts SET balance=? WHERE accountnumber=?""",(balanceafter,accountnumber))
        connection.commit()
        print("-Your account has been debited with rs.",amount)
        print("------------------------------------")
     except ValueError:
        print("Please,Enter an valid amount!")
        print("------------------------------------")
     except sqlite3.Error as e:
       connection.rollback()
       print("Transaction failed:",e)
#logout the account
    elif choice==6:
      print("==THANKS FOR USING OUR BANK==")
      print("------------------------------------")
      break 
#show balance after each transaction 
    elif choice==3:
      account.see_balance()
#show transaction history 
    elif choice==4:
      print("==TRANSACTION HISTORY==")
      print("-ENTER-1-SEE ALL HISTORY")
      print("-ENTER-2-SEARCH BY DATE")
      print("-ENTER-3-SEE CREDITED TRANSACTIONS")
      print("-ENTER-4-SEE DEBITED TRANSACTIONS")
      print("-ENTER-5-BACK")
      while True:
       try:
        choice=int(input("Enter your choice:"))
        if choice==1:
          history=cursor.execute(f"""SELECT * FROM history WHERE accountnumber=?""",(accountnumber,)).fetchall()
          if history:
            print("-Transaction history:")
            count=1
            for i in history:
              print(f"{count}.{i[2]} with Rs.{i[3]},balancebefore Rs.{i[4]},balanceafter Rs.{i[5]} by,time:{i[6]},date:{i[7]}")
              count+=1
            print("------------------------------------")
          else: 
            print(" No transaction history found!")
        elif choice==2:
          date =input("-ENTER THE DATE(YYYY-MM-DD): ")
          history=cursor.execute(f"""SELECT * FROM history WHERE accountnumber=? AND date=? """,(accountnumber,date)).fetchall()
          if history:
            print("-Transaction history:")
            count=1
            for i in history:
              print(f"{count}.{i[2]} with Rs.{i[3]},balancebefore Rs.{i[4]},balanceafter Rs.{i[5]} by,time:{i[6]},date:{i[7]}")
              count+=1
            print("------------------------------------")
          else: 
            print(" No transaction history found!")
        elif choice==3:
          process="credited"
          history=cursor.execute(f"""SELECT * FROM history WHERE accountnumber=? AND history=?""",(accountnumber,process)).fetchall()
          if history:
            print("-Transaction history:")
            count=1
            for i in history:
              print(f"{count}.{i[2]} with Rs.{i[3]},balancebefore Rs.{i[4]},balanceafter Rs.{i[5]} by,time:{i[6]},date:{i[7]}")
              count+=1
            print("------------------------------------")
          else: 
            print(" No transaction history found!")
        elif choice==4:
          process="debited"
          history=cursor.execute(f"""SELECT * FROM history WHERE accountnumber=? AND history=?""",(accountnumber,process)).fetchall()
          if history:
            print("-Transaction history:")
            count=1
            for i in history:
              print(f"{count}.{i[2]} with Rs.{i[3]},balancebefore Rs.{i[4]},balanceafter Rs.{i[5]} by,time:{i[6]},date:{i[7]}")
              count+=1
            print("------------------------------------")
          else: 
            print(" No transaction history found!")
        elif choice==5:
          print("------------------------------------")
          break
        else:
          print("INVALID INPUT!,ENTER NUMBER AMONG 1 TO 5")
          print("------------------------------------")
       except ValueError:
         print("INVALID INPUT!,ENTER AN INTEGER")
         print("------------------------------------")
       except sqlite3.Error as e:
         print("Database Error:",e)
         print("------------------------------------")
    elif choice==5:
      print("==SETTINGS==")
      print("ENTER-1-CHANGE USERNAME")
      print("ENTER-2-CHANGE PHONENUMBER")
      print("ENTER-3-PASSWORD")
      print("ENTER-4-VIEW PROFILE")
      print("ENTER-5-DELETE ACCOUNT")
      print("ENTER-6-BACK")
      while True:
       try:
        choice=int(input("Enter your choice:"))
        print("------------------------------------") 
        if choice==1:
          print("==CHANGE USERNAME==")
          user_name=cursor.execute("""SELECT username FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
          print("USERNAME:",user_name[0])
          username=input("Enter the new username:")
          cursor.execute("""UPDATE accounts SET username=?  WHERE accountnumber=?""",(username,accountnumber))
          connection.commit()
          print("YOUR USERNAME HAS BEEN SUCCESSFULLY UPDATED!")
          print("------------------------------------")
        elif choice==2:
          print("==CHANGE PHONENUMBER==")
          phone_number=cursor.execute("""SELECT phonenumber FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
          print("PHONENUMBER:",phone_number[0])
          phonenumber=input("Enter the new phonenumber:")
          if len(phonenumber)!=10 or phonenumber.isdigit()==False:
            print("-INVALID PHONE NUMBER, ENTER A 10 DIGIT NUMBER!")
            print("-----------------------------------")
          else:
           cursor.execute("""UPDATE accounts SET phonenumber=?  WHERE accountnumber=?""",(phonenumber,accountnumber))
           connection.commit()
           print("YOUR PHONE NUMBER HAS BEEN SUCCESSFULLY UPDATED!")
           print("------------------------------------")
            
        elif choice==3:
         print("==CHANGE PASSWORD==")
         pass_word=cursor.execute("""SELECT password FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
         stored_pass_word=pass_word[0]
         enterpassword=getpass("Enter your current password:")
         try:
          ph.verify(stored_pass_word,enterpassword)
          passwo_rd=input("Enter the new password:")
          pas_sword=input("Confirm the password:")
          if passwo_rd==pas_sword:
           password=ph.hash(passwo_rd)
           cursor.execute("""UPDATE accounts SET password=?  WHERE accountnumber=?""",(password,accountnumber))
           connection.commit()
           print("YOUR PASSWORD HAS BEEN SUCCESSFULLY UPDATED!")
           print("------------------------------------")
          else:
            print("PASSWORD NOT CHANGE!")
            print("------------------------------------")
         except Exception:
            print("INCORRECT ACCOUNT!")
            print("------------------------------------")
        elif choice==4:
          print("==PROFILE==")
          user_name=cursor.execute("""SELECT username FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
          phone_number=cursor.execute("""SELECT phonenumber FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
          balance=cursor.execute("""SELECT balance FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
          print("USERNAME:",user_name[0])
          print("PHONENUMBER:",phone_number[0])
          print("ACCOUNTNUMBER:",accountnumber)
          print("BALANCE:",balance[0])
        elif choice==5:
          print("==DELETE ACCOUNT==")
          stored_password=cursor.execute("""SELECT password FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
          password=getpass("Enter your password:")
          print("ENTER-1-CONFIRM DELETE")
          print("ENTER-2-CANCEL DELETE")
          try:
           ph.verify(stored_password[0],password)
           choice=int(input("ENTER:"))
           if choice==1:
            cursor.execute("""DELETE FROM accounts WHERE accountnumber=?""",(accountnumber,))
            connection.commit()
            print("ACCOUNT HAS BEEN DELETED SUCCESSFULLY!")
            print("------------------------------------")
            return
           elif choice==2:
            print("------------------------------------")
            break
           else:
            print("INVALID CHOICE!,ENTER 1 OR 2")
            print("------------------------------------")
          except Exception:
            print("INVALID CHOICE!,ENTER 1 OR 2")
            print("------------------------------------")                
        elif choice==6:
          print("------------------------------------")
          break
        else:
          print("INVALIT CHOICE!,ENTER NUMBER AMONG 1 TO 6")
          print("------------------------------------")
       except ValueError:
         print("INVALID INPUT!,ENTER AN INTEGER")
         print("------------------------------------")
            
#handle invalid input
    else:  
      print("INVALID INPUT:ENTER NUMBER AMONG 1 TO 5!")
      print("------------------------------------")
   except ValueError:
     print("-Invalid input:please enter an integer!")
     print("------------------------------------")
#save the account information after account has been created
def createaccount():
     hashed_password=ph.hash(password)
     cursor.execute("""INSERT INTO accounts(accountnumber,username,password,phonenumber)
     VALUES(?,?,?,?)""",(accountnumber,username, hashed_password,phonenumber))
     connection.commit()
     user_name=username.upper()
     print(f"-''{user_name}', your  account has been created successfully!")
     print("-Your account number is:",accountnumber)
     print("-Your phone number is:",phonenumber)
     print("------------------------------------") 
#menu of the bank account management system 
print("===WELCOME TO THE BANK OF INDIA===")
print("ENTER-1-LOGIN")
print("ENTER-2-CREATE ACCOUNT")
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
   username=input("-ENTER YOUR USERNAME:")
   try:
    accountnumber=int(input("-ENTER YOUR ACCOUNT NUMBER:"))
    password=getpass("-ENTER YOUR PASSWORD:")
    accountnumberlist=cursor.execute("""SELECT 1 FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
    if accountnumberlist:
      na_me=cursor.execute("""SELECT username FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
      name=na_me[0]
      pass_word=cursor.execute("""SELECT password FROM accounts WHERE accountnumber=?""",(accountnumber,)).fetchone()
      stored_password=pass_word[0]
#check if the account match or exist for login
      try:
       ph.verify(stored_password,password)
       if accountnumberlist and username == name:
#call the account function to perform the operations
        ACCOUNT(accountnumber)
       else:
        print("-ACCOUNT NOT FOUND!")
        print("------------------------------------")
      except Exception:
        print("-ACCOUNT NOT FOUND!")
        print("------------------------------------")
    else:
      print("ACCOUNT NOT FOUND!")
      print("------------------------------------")
   except ValueError:
        print("Invalid account!")
        print("------------------------------------")
   except sqlite3.Error as e:
       print("Database Error:",e)
       print("------------------------------------") 
#create account
  elif choice==2:
    print("===CREATE ACCOUNT===")
#take the user input for creating account
    username=input("-ENTER YOUR USERNAME:")
    accountnumber=input("-ENTER 10 DIGIT ACCOUNT NUMBER:")   
    if len(str(accountnumber))!=10:
     print("-INVALID ACCOUNT NUMBER, ENTER A 10 DIGIT NUMBER!")
     print("------------------------------------")
    elif accountnumber.isdigit()==False:
     print("-INVALID ACCOUNT NUMBER, ENTER A 10 DIGIT NUMBER!")
     print("------------------------------------")
    else:
     password=input("-ENTER 8 CHARACTER TO CREATE PASSWORD:")
     if len(str(password))!=8:
      print("-INVALID PASSWORD, ENTER AN 8 CHARACTER PASSWORD!")
      print("------------------------------------")
     else:
      phonenumber=input("-ENTER YOUR PHONE NUMBER:")
      phonenumberlist=cursor.execute("""SELECT 1 FROM accounts WHERE phonenumber=?""",(phonenumber,)).fetchone()
      if len(phonenumber)!=10 or phonenumber.isdigit()==False:
       print("-INVALID PHONE NUMBER, ENTER A 10 DIGIT NUMBER!")
       print("-----------------------------------")
      elif phonenumberlist:
       print("-PHONE NUMBER ALREADY EXISTS!")
       print("-----------------------------------") 
      else:
#create new table for each user for saving there transaction history 
        createaccount()
#exit from the application 
  elif choice==3:
    print("==THANKS==")
    break
  else:
   print("-INVALID CHOICE, ENTER 1 OR 2!")
   print("---------------------------------------")
 except ValueError:
  print("-INVALID INPUT, ENTER AN INTEGER!")
  print("----------------------------------------")
 except sqlite3.IntegrityError:
   print("ACCOUNT ALREADY EXISTS!")
   print("----------------------------------------")
  
 except sqlite3.Error as e:
   print("Database Error:",e)
   print("----------------------------------------")
    
    

                   
                   
              

      
