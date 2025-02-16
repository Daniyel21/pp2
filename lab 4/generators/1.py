def square_generator(n):
    result = []  
    for i in range(n):
        
        k = (i+1)**2
        result.append(k)
    return result

n = int(input("Input a number: "))
squares = square_generator(n)

for square in squares:
    print(square)