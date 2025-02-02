class Dorm:
    def __init__(self):
        self.inp = ""
    def getString(self):
        self.inp = input("Enter a string: ")
    def printString(self):
        self.inp = print(self.inp)
string_obj = Dorm()
string_obj.getString() 
string_obj.printString()

