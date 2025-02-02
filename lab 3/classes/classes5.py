class Account :
    def __init__(self):
        self.owner = str(input("Your name is = "))
        self.balance = int(input("Your balance is = "))
        self.i=0
    def deposit(self):
        while self.i<1 :
            self.minus= int(input("how many money do you want to put in your deposit? : "))
            if self.balance - self.minus < 0:
                print("You dont have enought money")
            else:
                self.balance = self.balance - self.minus 
                print("your balance now is: ", self.balance)
                break 
    def withdraw(self):
        while self.i<1 :
            self.minus= int(input("how many money do you want to withdraw? : "))
            if self.balance - self.minus < 0:
                print("You dont have enought money")
            else:
                self.balance = self.balance - self.minus 
                print("your balance now is: ", self.balance)
                break 

string_obj = Account()
string_obj.deposit() 
string_obj.withdraw()