txt=open("lab 6/builtin_functions/text.txt","+r")

up_letter = 0
low_letter = 0

for i in txt:
    if type(i) == str:
        tenis = i
        pizza = i.lower()

        if tenis == pizza:
            up_letter+=1
        else:
            low_letter+=1

print(f"low: {low_letter} ")
print(f"up: {up_letter} ")
