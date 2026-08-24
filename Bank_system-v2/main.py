import json
#take user input for login or create account 
#manage the bank account operations 
def ACCOUNT():
  # Bank account management system 
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
        print("==BALANCE==")
        print("-BALANCE RS.",data[accountnumber]["balance"])
        print("------------------------------------")   
#show the transaction history of the account 
      def see_history(self):
       with open("bank_data.json","r") as file:
        data=json.load(file)
        history=f"{process} with Rs.{amount}" 
        number=len(data[accountnumber]["transaction_history"])+1
        balance=data[accountnumber]["balance"]
        history=(f"{number}.amount: {history},balance:{balance}\n")
        data[accountnumber]["transaction_history"].append(history)
        data[accountnumber]["history"]+=history
        with open("bank_data.json","w") as file:
          json.dump(data,file)
#add the transaction history  to the list         
#create an object of the account class
  with open("bank_data.json","r") as file:
    data=json.load(file)
  balance=data[accountnumber]["balance"]
  account=Account(accountnumber,balance)
#A menu driven program that allows the user to credit or debit the account 
  print("===WELCOME TO THE BANK===")
  print("-USERNAME:",data[accountnumber]["name"])
  print("-ACCOUNT NUMBER:",data[accountnumber]["accountnumber"])
  print("-PHONE NUMBER:",data[accountnumber]["phonenumber"])
  print("-BALANCE RS.",data[accountnumber]["balance"])
  print("ENTER-1-CREDIT")
  print("ENTER-2-DEBIT") 
  print("ENTER-3-SEE BALANCE")
  print("ENTER-4-SEE TRANSACTION HISTORY")
  print("ENTER-5-LOGOUT") 
#create a list to add the balance after each transaction 
#list to add transaction history 
#create a loop to run the program until the user exits
  while True:
   with open("bank_data.json","r") as file:
    data=json.load(file)
#to handle invalid input
   try:
#take the menu user choice
    choice = int(input("-Enter your choice :"))
    print("------------------------------------")
#using conditional statements to perform the operation according to the user choice 
    if choice==1:
      print("==CREDIT==")
      process="credited"
      amount=int(input(f"-Enter the amount to be {process} Rs."))
      account.credit(amount)
      account.see_history()
      with open("bank_data.json","r") as file:
       data=json.load(file)
       data[accountnumber]["balance"]+=amount
      with open("bank_data.json","w") as file:
        json.dump(data,file)
    elif choice==2:
      print("==DEBIT==")
      process="debited"
      amount=int(input(f"-Enter the amount to be {process} Rs."))
      if data[accountnumber]["balance"]<amount:
        print("-Insufficient balance!")
        print("------------------------------------")
      else:
        account.debit(amount)
        account.see_history()
        with open("bank_data.json","r") as file:
         data=json.load(file)
        data[accountnumber]["balance"]-=amount
        with open("bank_data.json","w") as file:    
         json.dump(data,file)
    elif choice==5:
      print("==THANKS FOR USING OUR BANK==")
      print("------------------------------------")
      break 
#show balance after each transaction 
    elif choice==3:
      account.see_balance()
    elif choice==4:
      print("==TRANSACTION HISTORY==")
      with open("bank_data.json","r") as file:
        data=json.load(file)
        if len(data[accountnumber]["transaction_history"])==0:
         print(" No transaction history found!")
        else:
         print("-Transaction history:")
         print(data[accountnumber]["history"])       
         print("------------------------------------")    
#handle invalid input
    else:  
      print("-Invalid choice: please enter a no. between 1 to 5!")
      print("------------------------------------")
   except:
     print("-Invalid input:please enter an integer!")
     print("------------------------------------")
#menu of the bank account management system 
def createaccount():
  with open("bank_data.json","r") as file:
   data=json.load(file)
   data[accountnumber]={"name":username,"password":password,"accountnumber":accountnumber,"balance":0,"transaction_history":[],"history":"","phonenumber":phonenumber}
   data["accountnumber"].append(accountnumber)
   data["phonenumber"].append(phonenumber)
   data["name"].append(username)
   with open("bank_data.json","w") as file:
     json.dump(data,file)
     user_name=username.upper()
     print(f"-{user_name} your  account has been created successfully!")
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
    with open("bank_data.json","r") as file:
      data=json.load(file)
      print("===LOGIN===")
#take the user input for login
    try:
      username=input("-ENTER YOUR USERNAME:")
      accountnumber=input("-ENTER YOUR ACCOUNT NUMBER:")
      password=input("-ENTER YOUR PASSWORD:")
      stored_password=data[accountnumber]["password"]
      name=data[accountnumber]["name"]
      if accountnumber in data["accountnumber"] and username == name and password == stored_password:
#call the account function to perform the operations
       ACCOUNT()
      else:
        print("-ACCOUNT NOT FOUND!")
        print("------------------------------------")
    except:
        print("-ACCOUNT NOT FOUND!")
        print("------------------------------------")
  elif choice==2:
   
    print("===CREATE ACCOUNT===")
#take the user input for creating account
    username=input("-ENTER YOUR USERNAME:")
    accountnumber=input("-ENTER 10 DIGIT ACCOUNT NUMBER:")
    with open("bank_data.json","r") as file:
     data=json.load(file)
    if accountnumber in data["accountnumber"]:
     print("-ACCOUNT NUMBER ALREADY EXISTS!")
     print("------------------------------------")
    elif len(str(accountnumber))!=10:
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
      if len(phonenumber)!=10 or phonenumber.isdigit()==False:
       print("-INVALID PHONE NUMBER, ENTER A 10 DIGIT NUMBER!")
       print("-----------------------------------")
      elif phonenumber in data["phonenumber"]:
       print("-PHONE NUMBER ALREADY EXISTS!")
       print("-----------------------------------") 
      else:
        createaccount()
  elif choice==3:
    print("==THANKS==")
    break
  else:
   print("-INVALID CHOICE, ENTER 1 OR 2!")
   print("---------------------------------------")
 except:
  print("-INVALID INPUT, ENTER AN INTEGER!")
  print("----------------------------------------")
    
    

