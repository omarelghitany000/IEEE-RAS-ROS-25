class BankAccount :
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name= name
        self.balance= balance

    #add the amount to the balnace
    def Deposit(self, amount):
         self.balance += amount

    #deduct the amount from the balnace
    def  Withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("The balance isn't enough")

    # 5% fee discount
    def bankFees(self):
        fees = self.balance * 0.05
        self.balance -= fees

    # Details
    def display(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Account Name: {self.name}")
        print(f"Account Balance: {self.balance} $")

account = BankAccount(300291, "Ahmed", 1200)
account.display()
    
            
        

            