import math 

class point:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def show(self):
        print(f"Current position: ({self.x}, {self.y})")

    def move(self):
        self.x1 = float(input("Move to x = "))
        self.y1 = float(input("Move to y = "))

    def dist(self):
        distance = math.sqrt((self.x1 - self.x)**2 + (self.y1 - self.y)**2)
        print(f"Distance moved: {distance}")

    
string_obj = point()
string_obj.show() 
string_obj.move()
string_obj.dist()