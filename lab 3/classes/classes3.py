class Shape:
    def area(self):
        self.leng = print(0)
class Rectangle(Shape):
    def __init__(self):
        self.leng = ""
        self.wid = ""
    def ligh(self):
        self.leng = int(input("write lenght "))
        self.wid = int(input("write width "))
    def area(self):
        print("area of the Rectangle is " , self.leng*self.wid)
string_obj = Shape()
string_obj.area() 
deluk = Rectangle()
deluk.ligh()
deluk.area()
