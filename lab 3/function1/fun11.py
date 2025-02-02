def is_palindrome(word):
    word = word.replace(" ", "").lower() 
    return word == word[::-1] 

if is_palindrome("madam") == True:
    print("Yes")
else:
    print("No")
