def polindrom(number,number_rev):
    for i in number:
        for j in number_rev:
            if i!=j:
                return False
                break
            return True
        
    

number=str(input("enter sentence:"))
number_reverse=''.join(reversed(number))
print(polindrom(number,number_reverse))