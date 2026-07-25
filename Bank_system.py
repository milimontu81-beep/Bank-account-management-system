# Bank account management system 
# create a account class with attributes account number and balance    
class Account:
    def __init__(self, act_no, balance):
     self.act_no = act_no
     self.balance = balance
#add money to the account  
    def credit(self, amount):
     self.balance= self.balance+amount
     print(" your account has been credited with Rs.",amount) 
#withdraw money from the account 
    def debit(self, amount):
     if self.balance<amount:
      print("insufficient balance")
     else:
      self.balance= self.balance-amount
      print("your account has been debited with Rs.",amount)
#show the balance of the account 
    def see_balance(self):
      print("your account balance is Rs.", self.balance)
#show the transaction history of the account 
    def see_history(self):
      history=f"{process} with Rs.{amount}"
      
      historylist=f"amount: {history},balance:{self.balance}"
#add the transaction history  to the list    
      History.append(historylist)
      
#create an object of the account class
account=Account("123456789",1000)
#A menu driven program that allows the user to credit or debit the account 
print("welcome to the bank")
print("your account number is",account.act_no)
print("your account balance is Rs.",account.balance)
print("1.credit")
print("2.debit") 
print("3.see balance")
print("4.see transaction history")
print("5.exit") 
#create a list to add the balance after each transaction 
balance=[]
#list to add transaction history 
History=[]
#create a loop to run the program until the user exits
while True:
#to handle invalid input
 try:
#take the menu user choice
  choice = int(input("Enter your choice :"))  
#using conditional statements to perform the operation according to the user choice 
  if choice==1:
    process="credited"
    amount=int(input(f"Enter the amount to be {process} Rs."))
    account.credit(amount)
    account.see_history()
    balance.append(account.balance)
  elif choice==2:
   process="debited"
   amount=int(input(f"Enter the amount to be {process} Rs."))
   account.debit(amount)
   account.see_history()
   balance.append(account.balance)
  elif choice==5:
    print("thanks for using our bank!") 
    break 
#show balance after each transaction 
  elif choice==3:
    account.see_balance()
  elif choice==4: 
      if len(History)==0:
       print("no transaction history found")
      else:
       print("transaction history:")
       number=1
       for i in History:
         print(f"{number}.{i}")
         number=number+1
#handle invalid input
  else:
   
    print("invalid choice: please enter a no. between 1 to 5!")
 except:
    print("invalid input:please enter an integer!")
   