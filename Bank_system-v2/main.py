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
