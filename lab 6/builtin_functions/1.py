f=open("lab 6/builtin_functions/text.txt","+r")

sum = 1
for x in f.read().split(" "):
    x= int(x)
    sum =sum*x

print(sum)
