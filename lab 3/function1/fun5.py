from itertools import permutations
def permit():
    stri = str(input("your string: "))
    perm = permutations(stri)
    for i in list(perm): 
        print(i) 

permit()

