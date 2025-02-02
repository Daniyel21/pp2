class Shape:
    def area(self):
        self.leng = print(0)
class Square(Shape):
    def __init__(self):
        self.leng = ""
    def ligh(self):
        self.leng = int(input("write leight "))
    def area(self):
        print("area of the Square is " , self.leng**2)
string_obj = Shape()
string_obj.area() 
deluk = Square()
deluk.ligh()
deluk.area()
